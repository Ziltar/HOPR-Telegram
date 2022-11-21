from telegram.ext import *
from hoprApi import *
from settings import TG_BOT_KEY

def main():
    print("Started")
    updater = Updater(TG_BOT_KEY, use_context = True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("ping", ping_command))
    dp.add_handler(CommandHandler("send", send_command))
    updater.start_polling()
    updater.idle()

def ping_command(update, context):
    context.bot.send_message(update.message.chat.id,
                                 '<code>' + str(ping(update['message']['text'].split(' ')[1])) + '</code>',
                                 parse_mode='HTML',
                                 disable_web_page_preview=True)  

def send_command(update, context):
    msg_to = update['message']['text'].split(' ')[1]
    msg = update['message']['text'].replace('/send ' + msg_to, '')
    context.bot.send_message(update.message.chat.id,
                                 '<code>' + send_message(msg_to, msg, []) + '</code>',
                                 parse_mode='HTML',
                                 disable_web_page_preview=True)  

if __name__ == '__main__':
    main()