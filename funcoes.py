import botoes
import texto
# import gtts
import logging
from telegram import ReplyMarkup, Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler


historico = []
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    historico.clear()
    context.bot.send_photo(
        chat_id=update.effective_message.chat_id,
        photo=open('Imagens/Imagem-Inicial.jpg', 'rb'),
        caption=f'Olá, {update.effective_user.full_name}! que ótimo ter você por aqui 😀'
    )
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=texto.start_texto,
        reply_markup=botoes.start_lines()
    )


def sendResposta(handler, text, reply_markup):
    if text != "":
        handler.edit_message_text(text=text, reply_markup=reply_markup)


def responsehistorico(opcao):
    print("opcao>>", opcao)
    historico.append(opcao)
    botoes.regressar_setor_line(historico)


def getReplyMarkup(option):
    replyMarkup = {
        texto.HOME: botoes.start_lines(),
        texto.ESTRUTURA_ADMINISTRATIVA: botoes.setor_line(),
        texto.SEAC_SGA: botoes.menu_seac(),
        texto.VOLTAR_FAQ_SEAC: botoes.faq_seac(),
        texto.CONTATO_SEAC: botoes.contato_seac(),
        # texto.CONTATO_SEAC: responsehistorico(texto.SEAC_SGA),
        texto.COEX_SGA: botoes.menu_coex(),
        texto.CONTATO_COEX: responsehistorico(texto.COEX_SGA),
        texto.FAQ_SEAC: botoes.faq_seac(),
        # texto.FAQ_SEAC: responsehistorico(texto.SEAC_SGA),
        # **dict.fromkeys([texto.FAQSEAC1, "faq_seac2", "faq_seac3", "faq_seac4", "faq_seac5", "faq_seac6", "faq_seac7", "faq_seac8", "faq_seac9", "faq_seac10"], responsehistorico(texto.VOLTAR_FAQ_SEAC)),
        texto.FAQSEAC1: botoes.regressar_faq_seac(), "faq_seac2": botoes.regressar_faq_seac(), "faq_seac3": botoes.regressar_faq_seac(), "faq_seac4": botoes.regressar_faq_seac(), "faq_seac5": botoes.regressar_faq_seac(), "faq_seac6": botoes.regressar_faq_seac(), "faq_seac7": botoes.regressar_faq_seac(), "faq_seac8": botoes.regressar_faq_seac(), "faq_seac9": botoes.regressar_faq_seac(), "faq_seac10": botoes.regressar_faq_seac(),
        texto.FAQ_COEX: responsehistorico(texto.FAQ_COEX)
    }
    # if option == texto.FAQSEAC1:
    #     print(option, replyMarkup.get(option))
    #     return botoes.regressar_faq_seac()

    return replyMarkup.get(option)


def getResponseText(option, update):
    text = {
        texto.HOME: f'Olá, {update.effective_user.full_name}! ' +
        texto.start_texto,
        texto.ESTRUTURA_ADMINISTRATIVA: "Escolha uma opção disponível para continuar 👇",
        texto.SEAC_SGA: texto.txt_seac,
        texto.VOLTAR_FAQ_SEAC: texto.txt_seac + texto.FAQ,
        texto.CONTATO_SEAC: texto.txt_seac + texto.seac_contato,
        texto.COEX_SGA: texto.txt_coex,
        texto.CONTATO_COEX: texto.txt_coex + texto.coex_contato,
        texto.FAQ_SEAC: texto.txt_seac + texto.FAQ,
        texto.FAQSEAC1: texto.txt_faq_seac1,
        "faq_seac2": texto.txt_faq_seac2,
        "faq_seac5": texto.txt_faq_seac5,
        "faq_seac6": texto.txt_faq_seac6,
        "faq_seac7": texto.txt_faq_seac7,
        "faq_seac8": texto.txt_faq_seac8,
        "faq_seac9": texto.txt_faq_seac9,
        "faq_seac10": texto.txt_faq_seac10,
        texto.FAQ_COEX: texto.txt_coex + texto.FAQ,
    }

    return text.get(option)


def getResponseTextReplyMarkup(option, update):
    return [getResponseText(option, update), getReplyMarkup(option)]


def balloon(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    handler = query
    handler.answer()

    argumentos = getResponseTextReplyMarkup(query.data, update)
    sendResposta(handler, argumentos[0], argumentos[1])


# registro dos botões utilizados por usuário.
    print(f'{update.effective_user.full_name} utilizou {query.data}')


def iniciar() -> None:
    token = "5241177916:AAHZUC5gimNEyosHBngN5-KELqBSYauthok"
    updater = Updater(token)
    dispatcher = updater.dispatcher

    # https://pt.stackoverflow.com/questions/297721/timeout-na-função-input-do-python
    # import signal

    # def timeout(signum, frame):
    #    raise Exception('Seu tempo acabou!')

    # signal.signal(signal.SIGALRM, timeout)
    # signal.alarm(5)

    # try:
    #    signal.alarm(5)
    #    name = input('Qual é o seu nome? ')
    #    signal.alarm(0)
    #    print('Seja bem-vindo,', name)
    # except Exception as e:
    #    print(e)

# Iniciar comandos da função quando solicitadas
    dispatcher.add_handler(MessageHandler(Filters.all, start))
    updater.dispatcher.add_handler(CallbackQueryHandler(balloon))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    iniciar()
