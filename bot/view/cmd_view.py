import base64
import datetime

from bot.handler import cmd_route
from utils.datetime_util import get_time_str


@cmd_route('help')
def help(update, context):
    """
    time - show time from param('%Y-%m-%d %H:%M:%S' or timestamp), param is current time  by default
    b64encode - base64 encode
    b64decode - base64 decode
    help - get help
    hello - say hello to me
    """
    txt = """
/time - show time from param('%Y-%m-%d %H:%M:%S' or timestamp). By default,  param is current time
/b64encode <txt> - base64 encode
/b64decode <txt> - base64 decode
/help - get help
/hello - say hello to me
* 发送 csv 转换成 excel 并返回链接
* 发送图片输入 md/url 可返回图片的 markdown/url 地址
    """
    update.message.reply_text(txt)


@cmd_route('hello')
def hello_handler(update, context):
    update.message.reply_text(f'Hello {update.message.from_user.first_name}')


@cmd_route('b64decode')
def b64decode(update, context):
    args = context.args
    if not args:
        update.message.reply_text('❌  here is not args')

    txt = args[0]
    update.message.reply_text(base64.b64decode(txt).decode())


@cmd_route('b64encode')
def b64encode(update, context):
    args = context.args
    if not args:
        update.message.reply_text('❌ there is not args')

    txt = args[0]
    update.message.reply_text(base64.b64encode(txt.encode()).decode())


@cmd_route('time')
def time_handler(update, context):
    args = context.args
    if args:
        t = ' '.join(map(str, args))
    else:
        t = datetime.datetime.now()

    update.message.reply_text(get_time_str(t))
