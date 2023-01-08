from telegram import *
from telegram.ext import *


buttons = [
    [
        InlineKeyboardButton("🟢 Enviar".upper(), callback_data="yes"),
        InlineKeyboardButton("🔴 Cancelar".upper(), callback_data="no")
    ]
]
bsug = [[InlineKeyboardButton("sugerir", callback_data='sugerir')]]

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.effective_message.chat_id, text="mensagem inicial mais botão sugerir.", reply_markup=InlineKeyboardMarkup(bsug))


def balloon(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    handler = query
    handler.answer()

    if "sugerir" == query.data:
        return sugerir(update,context)

def sugerir(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_message.chat_id, text="comente:")
    return comentar

def comentar(update: Update, context: CallbackContext):
    update.effective_message.reply_text(text=update.effective_message.text, reply_markup=InlineKeyboardMarkup(buttons))
    return confimar
def confimar(update: Update, context: CallbackContext):
    query = update.callback_query
    handler = query
    handler.answer()

    if "yes" == query.data:
        arquivo = open("teste.txt", "w")
        arquivo.write(f"{update.effective_user.full_name} surege:\n{update.effective_message.text};\n")
        handler.edit_message_text(
            text=f'Sugestão Registrada.')
        print(update.effective_message.text)
    if "no" == query.data:
        handler.edit_message_text(
            text="operation cancel")

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext):
    pass

def timeout(update: Update, context: CallbackContext):
   update.message.reply_text('out time has ended. good bye')

def iniciar() -> None:

    token = "API"
    updater = Updater(token, use_context =True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    #dispatcher.add_handler((CallbackQueryHandler(balloon)))

    conv_handler = ConversationHandler(
    entry_points=[
        CommandHandler("sugerir", sugerir),
        CallbackQueryHandler(balloon)],
    states={
        comentar:[MessageHandler(Filters.text,comentar)],
        confimar: [CallbackQueryHandler(confimar)],
        ConversationHandler.TIMEOUT: [CallbackQueryHandler(confimar, timeout), MessageHandler(Filters.text, timeout)],
        },
    fallbacks=[CommandHandler('cancel', cancel)],
    conversation_timeout=10
    )

    dispatcher.add_handler(  conv_handler  )

    #dispatcher.add_handler(CommandHandler("sugerir", sugerir))
    #dispatcher.add_handler(CallbackQueryHandler(confimar))
    #confimar: [CallbackQueryHandler(confimar)]

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    iniciar()
