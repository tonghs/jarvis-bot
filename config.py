import os


DEBUG = bool(os.environ.get('DEBUG', False))

# BOT
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
CHAT_ID = os.environ.get('CHAT_ID', '')

TELEGRAM_API_HOST = 'api.telegram.org'
GET_FILE_API = f'https://{TELEGRAM_API_HOST}/bot{BOT_TOKEN}/getFile?file_id={{file_id}}'
TELEGRAM_FILE_URL = f'https://{TELEGRAM_API_HOST}/file/bot{BOT_TOKEN}/{{file_path}}'
BOT_MSG_URL = f'https://{TELEGRAM_API_HOST}/bot{BOT_TOKEN}/sendMessage'

TMP_FILE_DIR = '/tmp'

# sentry
SENTRY_DSN = os.environ.get('SENTRY_DSN', '')

# tencent
TENCENT_SECRET_ID = os.environ.get('TENCENT_SECRET_ID', '')
TENCENT_SECRET_KEY = os.environ.get('TENCENT_SECRET_KEY', '')
