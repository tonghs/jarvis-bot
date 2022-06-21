import logging

import bot.view.cmd_view  # noqa pylint: disable=W0611
import config
from bot.handler import cmd_route
from bot.view import doc_view, msg_view
from telegram.ext import BaseFilter, Filters, MessageHandler, Updater


updater = Updater(token=config.BOT_TOKEN, use_context=True)
logger = logging.getLogger('jarvis')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def error_callback(update, context):
    logger.error(context.error)
    update.message.reply_text(f"❌ ERROR: {str(context.error)}")


for h in cmd_route.handler_list:
    updater.dispatcher.add_handler(h)


class SQLResultFilter(BaseFilter):
    def filter(self, update):
        return '+-' in update.text and '-+' in update.text and '|' in update.text and '--' in update.text


updater.dispatcher.add_handler(MessageHandler(Filters.photo, doc_view.photo_msg_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.document.image, doc_view.img_msg_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.document.text, doc_view.csv_msg_handler))
updater.dispatcher.add_handler(MessageHandler(Filters.text & SQLResultFilter(),
                               msg_view.text_sql_result_msg_handler))


if not config.DEBUG:
    updater.dispatcher.add_error_handler(error_callback)

updater.start_polling()
updater.idle()
