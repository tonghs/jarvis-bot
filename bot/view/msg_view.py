import os
import time

from config import TMP_FILE_DIR
from libs.google.client import client as google_client
from utils.string_util import sql_result_to_csv


def text_sql_result_msg_handler(update, content):
    msg = update.message.text
    csv_str = sql_result_to_csv(msg)

    update.message.reply_text('ok, handling them, wait a sec...')
    tmp_file = os.path.join(TMP_FILE_DIR, f"{time.time()}.csv")
    with open(tmp_file, 'wb') as f:
        f.write(csv_str)

    update.message.reply_document(document=open(tmp_file, 'rb'))
    update.message.reply_text('uploading to Google Sheet...')
    _, doc_url = google_client.update_csv_file(tmp_file)

    update.message.reply_text(doc_url)
