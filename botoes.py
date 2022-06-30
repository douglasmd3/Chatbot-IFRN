import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
import funcoes
import texto


def regressar_setor_line(historico):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠", callback_data=texto.HOME), InlineKeyboardButton(
            "↩", callback_data=historico.pop())]
    ])


regressar_faq_seac = [
    [InlineKeyboardButton("↩", callback_data=texto.VOLTAR_FAQ_SEAC)]
]
regressar_faq_seac = InlineKeyboardMarkup(regressar_faq_seac)


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
        [InlineKeyboardButton("📞 Contatos e Canais", callback_data="Contato_coex"),
         InlineKeyboardButton("❓ Perguntas Frequentes", callback_data=texto.FAQ_COEX)],
    ])


def faq_seac(historico):
    voltar = historico.pop()
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🏠", callback_data=texto.HOME),
         InlineKeyboardButton("↩", callback_data=voltar)],
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
         InlineKeyboardButton("↩", callback_data=voltar)]
    ])
