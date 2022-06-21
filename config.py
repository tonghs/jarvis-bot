import os


DEBUG = bool(os.environ.get('DEBUG', False))

# BOT
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

TELEGRAM_API_URI = 'https://api.telegram.org'
GET_FILE_API = f'https://{TELEGRAM_API_URI}/bot{BOT_TOKEN}/getFile?file_id={{file_id}}'
TELEGRAM_FILE_URL = f'https://{TELEGRAM_API_URI}/file/bot{BOT_TOKEN}/{{file_path}}'
BOT_MSG_URL = f'https://{TELEGRAM_API_URI}/bot{BOT_TOKEN}/sendMessage'

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
GOOGLE_SHEET_URL = 'https://docs.google.com/spreadsheets/d/'

TMP_FILE_DIR = '/tmp'

# sentry
SENTRY_DSN = os.environ.get('SENTRY_DSN')
