import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
import ClienteTelegram
import texto


def regressar_setor_line(historico):
    voltar = historico.pop()
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠", callback_data=texto.HOME), InlineKeyboardButton(
            "↩", callback_data=voltar)]
    ])


# MENU 4 - CONTATO-SEAC: CHAMADA POR Contato_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3
def contato_seac():
    return InlineKeyboardMarkup([[InlineKeyboardButton(
        "🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data=texto.SEAC_SGA)]])


def contato_coex():
    return InlineKeyboardMarkup([[InlineKeyboardButton(
        "🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data=texto.COEX_SGA)]])

# MENU 4 - FAQ-SEAC: CHAMADA POR FAQ_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3


# def faq_seac():
#     print("faq_seac")
#     return [
#         [InlineKeyboardButton("🏠", callback_data="HOME"),
#          InlineKeyboardButton("↩", callback_data="MENU3")],
#         [InlineKeyboardButton(
#             "01 - Justificativa de Faltas/Reposição de Atividades❓", callback_data="faq_seac1")],
#         [InlineKeyboardButton("02 - Mudança de tuno/Turma❓",
#                               callback_data="faq_seac2")],
#         [InlineKeyboardButton("03 - Aproveitamento de Estudos❓",
#                               callback_data="faq_seac3")],
#         [InlineKeyboardButton(
#             "04 - Certificação de conhecimentos❓", callback_data="faq_seac4")],
#         [InlineKeyboardButton("05 - Emissão de Diploma❓",
#                               callback_data="faq_seac5")],
#         [InlineKeyboardButton("06 – Transferências❓",
#                               callback_data="faq_seac6")],
#         [InlineKeyboardButton("07 – Renovação de Matrícula❓",
#                               callback_data="faq_seac7")],
#         [InlineKeyboardButton("08 – Inscrição em Disciplina❓",
#                               callback_data="faq_seac8")],
#         [InlineKeyboardButton("09 – Trancamento de Matrícula❓",
#                               callback_data="faq_seac9")],
#         [InlineKeyboardButton("10 - Cancelamento de Disciplina❓",
#                               callback_data="faq_seacc10")],
#         [InlineKeyboardButton("🏠", callback_data="HOME"),
#          InlineKeyboardButton("↩", callback_data="MENU3")],
#     ]


# MENU 5 - OP. FAQ-SEAC: CHAMADA POR OP. FAQ-SEAC + OPÇÕES DE VOLTAR INICIO OU MENU 5 PARA MENU 4
def regressar_faq_seac():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("↩", callback_data=texto.VOLTAR_FAQ_SEAC)]
    ])


def start_lines():
    return InlineKeyboardMarkup([[InlineKeyboardButton(
        "🏢 SETORES", callback_data=texto.ESTRUTURA_ADMINISTRATIVA)], ])


def setor_line():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("🏠", callback_data=texto.HOME)],
        [InlineKeyboardButton(
            "🏢 SECRETARIA ACADÊMICA | SEAC/SGA", callback_data=texto.SEAC_SGA)],
        [InlineKeyboardButton(
            "🏢 COORDENAÇÃO DE EXTENSÃO | COEX/SGA", callback_data=texto.COEX_SGA)],
    ])


def menu_seac():

    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠", callback_data=texto.HOME), InlineKeyboardButton(
            "↩", callback_data=texto.ESTRUTURA_ADMINISTRATIVA)],
        [InlineKeyboardButton("📞 Contatos e Canais", callback_data=texto.CONTATO_SEAC),
         InlineKeyboardButton("❓ Perguntas Frequentes", callback_data=texto.FAQ_SEAC)],
    ])


def menu_coex():
    return InlineKeyboardMarkup([

        [InlineKeyboardButton("🏠", callback_data=texto.HOME), InlineKeyboardButton(
            "↩", callback_data=texto.ESTRUTURA_ADMINISTRATIVA)],
        [InlineKeyboardButton("📞 Contatos e Canais", callback_data=texto.CONTATO_COEX),
         InlineKeyboardButton("❓ Perguntas Frequentes", callback_data=texto.FAQ_COEX)],
    ])


def faq_seac():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(
            "01 - Justificativa de Faltas/Reposição de Atividades❓", callback_data="faq_seac1")],
        [InlineKeyboardButton("02 - Mudança de tuno/Turma❓",
                              callback_data="faq_seac2")],
        [InlineKeyboardButton(
            "03 - Aproveitamento de Estudos❓", callback_data="faq_seac3")],
        [InlineKeyboardButton(
            "04 - Certificação de conhecimentos❓", callback_data="faq_seac4")],
        [InlineKeyboardButton("05 - Emissão de Diploma❓",
                              callback_data="faq_seac5")],
        [InlineKeyboardButton("06 – Transferências❓",
                              callback_data="faq_seac6")],
        [InlineKeyboardButton("07 – Renovação de Matrícula❓",
                              callback_data="faq_seac7")],
        [InlineKeyboardButton(
            "08 – Inscrição em Disciplina❓", callback_data="faq_seac8")],
        [InlineKeyboardButton(
            "09 – Trancamento de Matrícula❓", callback_data="faq_seac9")],
        [InlineKeyboardButton(
            "10 - Cancelamento de Disciplina❓", callback_data="faq_seac10")],
        [InlineKeyboardButton("🏠", callback_data=texto.HOME),
         InlineKeyboardButton("↩", callback_data=texto.SEAC_SGA)]
    ])
