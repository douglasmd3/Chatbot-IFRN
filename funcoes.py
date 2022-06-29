from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler
import logging, gtts, texto, botoes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    context.bot.send_photo(
        chat_id=update.effective_message.chat_id,
        photo=open('Imagens/Imagem-Inicial.jpg', 'rb'),
        caption=f'Olá, {update.effective_user.full_name}! que ótimo ter você por aqui 😀'
    )
    context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=texto.start_texto,
        reply_markup=botoes.start_lines
    )
    #print (f'{update.effective_user.full_name} Entrou. {update.effective_message}')
def balloon (update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    handler = query
    handler.answer()

    if "HOME" in query.data:
        handler.edit_message_text(
            text=f'Olá, {update.effective_user.full_name}! ' + texto.start_texto,
            reply_markup=botoes.start_lines
        )
    if "Estrutura_Administrativa" in query.data or "MENU2" in query.data:
        handler.edit_message_text(
            text="Escolha uma opção disponível para continuar 👇",
            reply_markup=botoes.setor_line
        )
    if "SEAC/SGA" in query.data or "MENU3"in query.data:
        handler.edit_message_text(
            text=texto.txt_seac,
            reply_markup=botoes.menu_seac
        )
    if "Contato_seac" in query.data:
        handler.edit_message_text(
            text=texto.txt_seac + texto.seac_contato,
            reply_markup=botoes.contato_seac
        )
#    if "COEX/SGA" in query.data or "VOLTAR_MENU" in query.data:
#        handler.edit_message_text(
#            text=texto.txt_coex,
#            reply_markup=botoes.menu_seac
#        )
#    if "Contato_coex" in query.data:
#        handler.edit_message_text(
#            text=texto.txt_coex + texto.coex_contato,
#            reply_markup=botoes.regressar_setor_line
#        )
    if "FAQ_seac" in query.data or "MENU4" in query.data:
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac
        )
    if "faq_seac1" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac1 + texto.txt_comum,
            reply_markup=botoes.regressar_faq_seac
        )
        audio_faq_seac1 = gtts.gTTS(texto.txt_faq_seac1, lang='pt-br')
        audio_faq_seac1.save('Audios/audio_faq_seac1.mp3')
        context.bot.send_audio(
            chat_id=update.effective_message.chat_id,
            audio=open('Audios/audio_faq_seac1.mp3', 'rb'),
        )
    if "faq_seac2" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac2,
            reply_markup=botoes.regressar_faq_seac,
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
        audio_faq_seac4 = gtts.gTTS(texto.txt_faq_seac4, lang='pt') # linha necessária apenas para converter o texto.
        audio_faq_seac4.save('Audios/audio_faq_seac4.mp3') # quando o arquivo for criado não é necessário pois pode haver demora ao refazer a conversão de texto e sobrescrever o mesmo arquivo.
        context.bot.send_audio( # se o arquivo já existir, basta envia - lo diretamente sem nova conversão.
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
#    if "FAQ_coex" in query.data:
#        handler.edit_message_text(
#            text=texto.txt_coex + texto.FAQ,
#            reply_markup=botoes.regressar_setor_line
#        )
    print(f'{update.effective_user.full_name} utilizou {query.data}') # registro dos botões utilizados por usuário.
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