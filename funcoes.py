import logging, gtts, texto, botoes
from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler, CommandHandler


historico = []
users = []
cont_users = 0
likes = 0
dislikes = 0

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    global  cont_users
    cont_users +=1
    users.append(f'{update.effective_user.full_name}')
#    print(f'{users.pop()} foi o usuário Nº{cont_users}')
    print(f'{users.pop()} interagiu com o  bot {cont_users}x')
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
def balloon(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    handler = query
    handler.answer()

    global likes, dislikes

    if "Avaliar" in query.data: #or "/sugeir" in query.data:
        handler.edit_message_text(
            text=f'{update.effective_user.full_name}, ' + 'qual a sua avaliação:?',
            reply_markup=botoes.buttons
        )
    if "good" in query.data:
        likes +=1
        handler.edit_message_text(
            text=f'{update.effective_user.full_name} ' + f'{texto.txt_avaliacao}',
            #reply_markup=botoes.regressar_setor_line(historico)
        )
    if "bad" in query.data:
        dislikes +=1
        handler.edit_message_text(
            text=f'{update.effective_user.full_name} ' + f'{texto.txt_avaliacao}',
        )
    W = f"likes => {likes} and dislikes => {dislikes}"
    arquivo = open("fones.txt", "w", encoding='utf-8')
    arquivo.write(W)
    arquivo.close()

    print(f"likes => {likes} and dislikes => {dislikes}")

    if texto.HOME in query.data:
        handler.edit_message_text(
            text=f'Olá, {update.effective_user.full_name}! ' + texto.start_texto,
            reply_markup=botoes.start_lines()
        )
    elif texto.ESTRUTURA_ADMINISTRATIVA in query.data or "MENU2" in query.data:
        handler.edit_message_text(
            text="Escolha uma opção disponível para continuar 👇",
            reply_markup=botoes.setor_line()
        )
    elif texto.VOLTAR_FAQ_SEAC in query.data:
        historico.append(texto.FAQ_SEAC)
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac(historico)
        )
    elif texto.SEAC_SGA in query.data:
        handler.edit_message_text(
            text=texto.txt_seac,
            reply_markup=botoes.menu_seac()
        )
    elif texto.CONTATO_SEAC in query.data:
        historico.append(texto.SEAC_SGA)
        handler.edit_message_text(
            text=texto.txt_seac + texto.seac_contato,
            reply_markup=botoes.regressar_setor_line(historico)
        )
    elif texto.COEX_SGA in query.data:
        handler.edit_message_text(
            text=texto.txt_coex,
            reply_markup=botoes.menu_coex()
        )
    elif texto.CONTATO_COEX in query.data:
        historico.append(texto.COEX_SGA)
        print(historico, texto.CONTATO_COEX)
        handler.edit_message_text(
            text=texto.txt_coex + texto.coex_contato,
            reply_markup=botoes.regressar_setor_line(historico)
        )
    elif texto.FAQ_SEAC in query.data:
        historico.append(texto.SEAC_SGA)
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac(historico)
        )
    #    if "FAQ_coex" in query.data:
    #        handler.edit_message_text(
    #            text=texto.txt_coex + texto.FAQ,
    #            reply_markup=botoes.regressar_setor_line
    #        )
    elif texto.FAQ_COEX in query.data:
        historico.append(texto.COEX_SGA)
        handler.edit_message_text(
            text=texto.txt_coex + texto.FAQ,
            reply_markup=botoes.regressar_setor_line(historico)
        )
        context.bot.send_sticker(
            chat_id=update.effective_message.chat_id,
            sticker='CAACAgIAAxkBAAIIWGJ6ipBYCf4X-anOjilu_zYolIs2AAK9AAP3AsgPHZqqRFvYN5okBA'
        )
        context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text="Isso é constrangedor e lamentamos 😩 este item não possui campos informativos 😓"\
        "se utilizou este item e for lhe ajudar 🫣 siga as instruções dadas no menu acima em 1, 2 ou 3 sinalizadas ⚠"
        )
    elif "faq_seac1" in query.data:
        historico.append(texto.SEAC_SGA)
        handler.edit_message_text(
            text=texto.txt_faq_seac1,
            reply_markup=botoes.regressar_faq_seac
        )
        audio_faq_seac1 = gtts.gTTS(texto.txt_faq_seac1, lang='pt-br')
        audio_faq_seac1.save('Audios/audio_faq_seac1.mp3')
        context.bot.send_audio(
            chat_id=update.effective_message.chat_id,
            audio=open('Audios/audio_faq_seac1.mp3', 'rb'),
        )
    elif "faq_seac2" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac2,
            reply_markup=botoes.regressar_faq_seac
        )
    if "faq_seac3" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac3,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seac4" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac4 + texto.txt_comum,
            reply_markup=botoes.regressar_faq_seac,
        )
        audio_faq_seac4 = gtts.gTTS(texto.txt_faq_seac4, lang='pt')  # linha necessária apenas para converter o texto.
        audio_faq_seac4.save(
            'Audios/audio_faq_seac4.mp3')  # quando o arquivo for criado não é necessário pois pode haver demora ao refazer a conversão de texto e sobrescrever o mesmo arquivo.
        context.bot.send_audio(  # se o arquivo já existir, basta envia - lo diretamente sem nova conversão.
            chat_id=update.effective_message.chat_id,
            audio=open('Audios/audio_faq_seac4.mp3', 'rb'),
        )
    if "faq_seac5" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac5,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seac6" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac6,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seac7" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac7,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seac8" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac8,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seac9" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac9,
            reply_markup=botoes.regressar_faq_seac,
        )
    if "faq_seacc10" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac10,
            reply_markup=botoes.regressar_faq_seac,
        )

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
    dispatcher.add_handler(CommandHandler('sugerir', balloon))
    updater.dispatcher.add_handler(CallbackQueryHandler(balloon))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    iniciar()