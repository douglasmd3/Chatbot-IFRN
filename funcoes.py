from telegram import Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler
import logging
import texto
import botoes

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
        reply_markup=botoes.start_lines
    )


def balloon(update: Update, context: CallbackContext) -> None:
    query = update.callback_query.data
    update.callback_query.answer()

    handler = update.callback_query
    handler.answer()

    if "HOME" in query:
        handler.edit_message_text(
            text=f'Olá, {update.effective_user.full_name}! ' +
            texto.start_texto,
            reply_markup=botoes.start_lines
        )
    if "VOLTAR_SETOR_LINE" in query:
        handler.edit_message_text(
            text="Escolha uma opção disponível para continuar 👇",
            reply_markup=botoes.setor_line
        )
    if "VOLTAR_FAQ_SEAC" in query:
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac
        )
    if "Estrutura_Administrativa" in query:
        handler.edit_message_text(
            text="Escolha uma opção disponível para continuar 👇",
            reply_markup=botoes.setor_line
        )
    if "SEAC/SGA" in query:
        handler.edit_message_text(
            text=texto.txt_seac,
            reply_markup=botoes.menu_seac
        )
    if "Contato_seac" in query:
        handler.edit_message_text(
            text=texto.txt_seac + texto.seac_contato,
            reply_markup=botoes.regressar_setor_line
        )
    if "COEX/SGA" in query:
        handler.edit_message_text(
            text=texto.txt_coex,
            reply_markup=botoes.menu_coex
        )
    if "Contato_coex" in query:
        handler.edit_message_text(
            text=texto.txt_coex + texto.coex_contato,
            reply_markup=botoes.regressar_setor_line
        )
    if "FAQ_seac" in query:
        handler.edit_message_text(
            text=texto.txt_seac + texto.FAQ,
            reply_markup=botoes.faq_seac
        )
    if "faq_seac1" in query:
        handler.edit_message_text(
            text=texto.txt_faq_seac1,
            reply_markup=botoes.regressar_faq_seac
        )
    if "faq_seac2" in query:
        handler.edit_message_text(
            text=texto.txt_faq_seac2,
            reply_markup=botoes.regressar_faq_seac
        )
    if "FAQ_coex" in query:
        handler.edit_message_text(
            text=texto.txt_coex + texto.FAQ,
            reply_markup=botoes.regressar_setor_line
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
