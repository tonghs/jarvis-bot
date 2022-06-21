import os.path
import pickle
import time

from config import GOOGLE_SHEET_URL
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from libs.google.google_auth import main as auth


# If modifying these scopes, you need to reload credential.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


class GoogleCredentialError(Exception):
    def __init__(self, message):
        self.message = message


class GoogleClient:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        pickle_file = os.path.join(path, 'token.pickle')
        creds = None
        if os.path.exists(pickle_file):
            with open(pickle_file, 'rb') as token:
                creds = pickle.load(token)

        if not creds:
            raise GoogleCredentialError('credential 不存在')
        if not creds.valid and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            # raise GoogleCredentialError('credential 无效')

        self.sheet_service = build('sheets', 'v4', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)

    def get_sheet(self, sheet_id, sample_range):
        # Call the Sheets API
        sheet = self.sheet_service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=sample_range).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            print('Name, Major:')
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print(f'{row[0]}, {row[4]}')

    def create_sheet(self, title):
        spreadsheet_body = {
            'properties': {
                'title': title
            }
        }

        spreadsheet = self.sheet_service.spreadsheets().create(body=spreadsheet_body).execute()

        return spreadsheet.get('spreadsheetId'), spreadsheet.get('spreadsheetUrl')

    def update_csv_file(self, file_path, file_name='', parent_id='1nOwSsQcBYkFCXgRRbFCSIdMJU-LAi5hn'):
        file_name = file_name if file_name else file_path.split('/')[-1]
        file_metadata = {
            'name': file_name,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [parent_id]
        }

        media = MediaFileUpload(file_path,
                                mimetype='text/csv',
                                resumable=True)
        resp = self.drive_service.files().create(body=file_metadata,
                                                 media_body=media).execute()
        doc_id = resp.get('id')
        return doc_id, f'{GOOGLE_SHEET_URL}{doc_id}/edit'


try:
    client = GoogleClient()
except GoogleCredentialError:
    auth()
    time.sleep(3)
    client = GoogleClient()


if __name__ == '__main__':
    client.update_csv_file('/home/tonghs/recipes_mahui.csv')
