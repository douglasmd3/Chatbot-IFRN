from telegram import Update, InlineKeyboardMarkup
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler
import logging
import gtts
import texto
import botoes

historico = []
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
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
        reply_markup=botoes.start_lines()
    )
    #print (f'{update.effective_user.full_name} Entrou. {update.effective_message}')


def balloon(update: Update, context: CallbackContext) -> None:

    query = update.callback_query
    handler = query
    handler.answer()

    if "HOME" in query.data:
        handler.edit_message_text(
            text=f'Olá, {update.effective_user.full_name}! ' +
            texto.start_texto,
            reply_markup=botoes.start_lines()
        )
    elif "Estrutura_Administrativa" in query.data or "MENU2" in query.data:
        handler.edit_message_text(
            text="Escolha uma opção disponível para continuar 👇",
            reply_markup=botoes.setor_line()
        )
    elif "VOLTAR_FAQ_SEAC" in query.data:
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac
        )
    elif "SEAC/SGA" in query.data:
        handler.edit_message_text(
            text=texto.txt_seac,
            reply_markup=botoes.menu_seac()
        )
    elif "Contato_seac" in query.data:
        historico.append("SEAC/SGA")
        handler.edit_message_text(
            text=texto.txt_seac + texto.seac_contato,
            reply_markup=botoes.regressar_setor_line(historico)
        )
    elif "COEX/SGA" in query.data:
        handler.edit_message_text(
            text=texto.txt_coex,
            reply_markup=botoes.menu_coex()
        )
    elif "Contato_coex" in query.data:
        historico.append("COEX/SGA")
        print(historico, "Contato_coex")
        handler.edit_message_text(
            text=texto.txt_coex + texto.coex_contato,
            reply_markup=botoes.regressar_setor_line(historico)
        )
    elif "FAQ_seac" in query.data:
        historico.append("SEAC/SGA")
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac(historico)
        )
    elif "faq_seac1" in query.data:
        historico.append("SEAC/SGA")
        handler.edit_message_text(
            text=texto.txt_faq_seac1,
            reply_markup=botoes.regressar_faq_seac
        )
    elif "faq_seac2" in query.data:
        handler.edit_message_text(
            text=texto.txt_faq_seac2,
            reply_markup=botoes.regressar_faq_seac
        )
    elif "FAQ_coex" in query.data:
        historico.append("COEX/SGA")
        handler.edit_message_text(
            text=texto.txt_coex + texto.FAQ,
            reply_markup=botoes.regressar_setor_line(historico)
        )


def iniciar() -> None:
    token = "5241177916:AAHZUC5gimNEyosHBngN5-KELqBSYauthok"
    updater = Updater(token)
    dispatcher = updater.dispatcher

# Iniciar comandos da função quando solicitadas
    dispatcher.add_handler(MessageHandler(Filters.all, start))
    updater.dispatcher.add_handler(CallbackQueryHandler(balloon))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    iniciar()
