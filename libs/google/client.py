import os.path

from config import GOOGLE_SHEET_URL, GOOGLE_DRIVE_DATA_DIR
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


# If modifying these scopes, you need to reload credential.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']


class GoogleCredentialError(Exception):
    def __init__(self, message):
        self.message = message


class GoogleClient:
    def __init__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        token_file = os.path.join(path, 'token.json')
        credentials_file = os.path.join(path, 'credentials.json')

        creds = None
        if os.path.exists(token_file):
            creds = Credentials.from_authorized_user_file(token_file, SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(token_file, 'w') as token:
                token.write(creds.to_json())

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

    def update_csv_file(self, file_path, file_name=''):
        file_name = file_name if file_name else file_path.split('/')[-1]
        file_metadata = {
            'name': file_name,
            'mimeType': 'application/vnd.google-apps.spreadsheet',
            'parents': [GOOGLE_DRIVE_DATA_DIR]
        }

        media = MediaFileUpload(file_path,
                                mimetype='text/csv',
                                resumable=True)
        resp = self.drive_service.files().create(body=file_metadata,
                                                 media_body=media).execute()
        doc_id = resp.get('id')
        return doc_id, f'{GOOGLE_SHEET_URL}{doc_id}/edit'


client = GoogleClient()


if __name__ == '__main__':
    client.update_csv_file('/home/tonghs/recipes.csv')
