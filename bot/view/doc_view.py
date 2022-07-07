import os

import requests
from bot.const import IMG_URL_TYPE
from config import GET_FILE_API, TELEGRAM_FILE_URL, TMP_FILE_DIR
from telegram import InputFile
from utils.doc_util import csv_to_excel


def _get_telegram_file(file_id, caption):
    url = ''
    r = requests.get(GET_FILE_API.format(file_id=file_id))
    if r.status_code == 200:
        rsp = r.json()
        file_path = rsp.get('result', {}).get('file_path')
        url = TELEGRAM_FILE_URL.format(file_path=file_path)

    if caption == IMG_URL_TYPE.MARKDOWN:
        return f"![]({url})"
    else:
        return url


def _download_tmp_file(url, file_name):
    r = requests.get(url, allow_redirects=True)
    tmp_file = os.path.join(TMP_FILE_DIR, file_name)
    with open(tmp_file, 'wb') as f:
        f.write(r.content)

    return tmp_file


def photo_msg_handler(update, context):
    caption = update.message.caption
    photos = update.message.photo

    photo = photos[-1]
    url = _get_telegram_file(photo.file_id, caption)

    if caption in [IMG_URL_TYPE.MARKDOWN, IMG_URL_TYPE.URL]:
        update.message.reply_text(url)


def img_msg_handler(update, context):
    caption = update.message.caption
    url = _get_telegram_file(update.message.document.file_id, caption)

    if caption in [IMG_URL_TYPE.MARKDOWN, IMG_URL_TYPE.URL]:
        update.message.reply_text(url)


def csv_msg_handler(update, context):
    file_name = update.message.document.file_name
    ext_name = '.csv'
    if file_name.endswith(ext_name):
        update.message.reply_text(f'ok, handling {file_name}, wait a sec...')
        update.message.reply_text(f'downloading {file_name} to local...')
        url = _get_telegram_file(update.message.document.file_id, 'csv')
        tmp_file = _download_tmp_file(url, file_name)

        update.message.reply_text('converting csv to xlsx...')
        with open(csv_to_excel(tmp_file), 'rb') as f:
            input_file = InputFile(f, filename=file_name.replace(ext_name, ".xlsx"))

        msg = f"""
**👍 {file_name} is ready!**

csv file_url: {url}
        """
        update.message.reply_text(msg)
        update.message.reply_document(document=input_file)
