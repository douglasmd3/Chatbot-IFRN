#pip install python-telegram-bot
from telegram import *
from telegram.ext import *
import time, logging, cod
from requests import *

logging.basicConfig(
    format='Informação de execucão do sistema:\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
logger = logging.getLogger(__name__)

image = f"https://scontent.fnat2-1.fna.fbcdn.net/v/t1.6435-9/33421594_1659227080812208_841173034298507264_n.jpg?_nc_cat=103&ccb=1-6&_nc_" \
        f"sid=09cbfe&_nc_ohc=tIatDovv740AX_FU5Y4&_nc_ht=scontent.fnat2-1.fna&oh=00_AT8IcXokpaMvG_geIXUBWLKE21_3ljsxETynxjJWLqsJbg&oe=62A7A72A"

txt_menu= """Escolha uma opção do /menu para continuar.\n(Clique no item):
/FAQ - Perguntas respoondidas frequentemente e Dúvidas;
/help - Ajuda - lhe a encontrar opções válidas;
/sugerir - Deixe alguma sugestão para atualizações futuras;
/avaliar - Experimente avaliar o atendimento;"""

likes = 0

dislikes = 0

def start (update: Update, context: CallbackContext) -> None:
    global var
    var = get(image).content
    txt_start = f"""Olá, {update.effective_user.full_name}. Que bom você por aqui. 
    \nSeja bem-vindo(a) ao sistema de atendimentos do IFRN/SGA. 
    \nVeja algumas opções disponíveis que poderá ajudar - lhe.
    \n"""

    context.bot.send_photo(chat_id=update.message.chat_id,photo=var, caption=txt_start + txt_menu)

def menu (update: Update, context: CallbackContext) -> None:
    context.bot.send_message(chat_id=update.message.chat_id, text=txt_menu)
    print(f"{update.message.date.now()}")

# Comando, apontando para /menu /start
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Não se preocupe, Buscando Ajuda 🆘 AGUARDE!")
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAIIEWJ53_ntngsb5aDtmlfa5oejtpJOAAKJCgACcW6JS9OXXOiMKwOwJAQ')
    time.sleep(5)
    update.message.reply_text(" ⏳ A finalizar o Processamento do Comando ⏳")
    time.sleep(5)
    update.message.reply_text("Use /menu ou /start para consultar as opções disponíveis 😉")

def avaliar (update: Update, context: CallbackContext) -> None:

    buttons = [[InlineKeyboardButton("👍", callback_data="good")],[InlineKeyboardButton("👎", callback_data="bad"),]]

    context.bot.send_message(chat_id=update.effective_chat.id,reply_markup=InlineKeyboardMarkup(buttons), text="Qual a sua avaliação:?")

def queryHandler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query.data
    update.callback_query.answer()

    global likes, dislikes

    txt_avaliacao = f"""{update.effective_user.full_name}, Obrigado pela avaliação. 
    \nContinuaremos a desenvolver novas atualizações para prestar - lhe sempre um bom atendimento.
    \nSinta- se livre para deixar sua sugestão de atendimento  que não encontrou ou que precise de melhorias (/sugerir).
    \nSe preferir, entre em contato com os responsáveis do projeto: @marmundo @Michael_Moreira"""

    if "good" in query:
        likes +=1

    if "bad" in query:
        dislikes +=1

    context.bot.send_message(chat_id=update.effective_chat.id, text = txt_avaliacao)

    W = f"likes => {likes} and dislikes => {dislikes}"
    arquivo = open("fones.txt", "w", encoding='utf-8')
    arquivo.write(W)
    arquivo.close()

    print(f"likes => {likes} and dislikes => {dislikes}")

    handler = update.callback_query
    handler.answer()
    handler.edit_message_text(text=f"OPÇÃO SELECIONADA: {handler.data}")

def sugerir (update: Update, context: CallbackContext) -> None:
#    arquivo = open("fones.txt", "w", encoding='utf-8')
#    arquivo.write()
     context.bot.send_message(chat_id=update.effective_chat.id, text = "Para sugerir entre em contato com os responsáveis do projeto: @marmundo\n@Michael_Moreira")

def exc(update: Update, context: CallbackContext) -> None:
    texto = """
    Solicitação indisponível na listagem de comandos.
    Tente:
    /help - Ajuda - lhe a encontrar opções válidas;
    \nNão encontrou o que procura? Tente:
    /sugerir - Deixe sua sugestão de melhoria;
    /avaliar - Experimente avaliar o atendimento;
    """

    update.message.reply_text("Aguarde, Buscado reconhecimento de comando 🔍")
    time.sleep(5)
    context.bot.send_sticker(chat_id=update.message.chat_id, sticker='CAACAgIAAxkBAAIIWGJ6ipBYCf4X-anOjilu_zYolIs2AAK9AAP3AsgPHZqqRFvYN5okBA')
    update.message.reply_text(f"{texto}")

def main() -> None:
    token = "5241177916:AAHZUC5gimNEyosHBngN5-KELqBSYauthok"
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('menu', menu))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(CommandHandler('avaliar', avaliar))
    dispatcher.add_handler(CommandHandler('sugerir', sugerir))

    dispatcher.add_handler(CallbackQueryHandler(queryHandler))
    dispatcher.add_handler(MessageHandler(Filters.all, exc))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()