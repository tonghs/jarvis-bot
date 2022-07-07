import os
import time

from config import TMP_FILE_DIR
from telegram import InputFile
from utils.doc_util import csv_to_excel
from utils.string_util import sql_result_to_csv


def text_sql_result_msg_handler(update, content):
    msg = update.message.text
    csv_str = sql_result_to_csv(msg)

    update.message.reply_text('ok, handling them, wait a sec...')
    tmp_file = os.path.join(TMP_FILE_DIR, f"{time.time()}.csv")
    with open(tmp_file, 'wb') as f:
        f.write(csv_str)

    update.message.reply_document(document=open(tmp_file, 'rb'))

    update.message.reply_text('converting csv to xlsx...')
    with open(csv_to_excel(tmp_file), 'rb') as f:
        input_file = InputFile(f, filename=f"{tmp_file}.xlsx")

    update.message.reply_document(document=input_file)
