import bot.texto as texto

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def regressar_setor_line(historico):
    voltar = historico.pop()
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠 HOME", callback_data=texto.HOME),
                InlineKeyboardButton("↩ RETURN", callback_data=voltar),
            ]
        ]
    )


# MENU 4 - CONTATO-SEAC: CHAMADA POR Contato_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3
# def contato_seac():
#     return InlineKeyboardMarkup([[InlineKeyboardButton(
#         "🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data=texto.SEAC_SGA)]])


# def contato_coex():
#     return InlineKeyboardMarkup([[InlineKeyboardButton(
#         "🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data=texto.COEX_SGA)]])

def buttons_avaliar():
    return InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🏠 HOME", callback_data=texto.HOME),
        InlineKeyboardButton("🏢 SETORES", callback_data=texto.ESTRUTURA_ADMINISTRATIVA),
    ],
    [InlineKeyboardButton("😊 - Bom, gostei!", callback_data=texto.BOM)],
    [InlineKeyboardButton("🤔 - Normal, tanto faz.", callback_data=texto.NORMAL),],
    [InlineKeyboardButton("☹ - Ruim, Não gostei.", callback_data=texto.RUIM),],
    ])


def resposta_avaliacao():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🏠 HOME", callback_data=texto.HOME),
            InlineKeyboardButton("🏢 SETORES", callback_data=texto.ESTRUTURA_ADMINISTRATIVA),
        ]
    ])

# MENU 4 - FAQ-SEAC: CHAMADA POR FAQ_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3


# MENU 5 - OP. FAQ-SEAC: CHAMADA POR OP. FAQ-SEAC + OPÇÕES DE VOLTAR INICIO OU MENU 5 PARA MENU 4
# def regressar_faq_seac():
#     return InlineKeyboardMarkup([
#         [InlineKeyboardButton("↩", callback_data=texto.VOLTAR_FAQ_SEAC)]
#     ])


def start_lines():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏢 SETORES", callback_data=texto.ESTRUTURA_ADMINISTRATIVA),  # botao_feed
                InlineKeyboardButton("📊 AVALIAR", callback_data=texto.AVALIAR),
                InlineKeyboardButton("💬 SUGERIR", callback_data=texto.SUGERIR),
            ],
        ]
    )


def setor_line():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠", callback_data=texto.HOME),
                InlineKeyboardButton("📊", callback_data=texto.AVALIAR),
                InlineKeyboardButton("💬", callback_data=texto.SUGERIR),
            ],
            [InlineKeyboardButton("🏢 SECRETARIA ACADÊMICA | SEAC/SGA", callback_data=texto.SEAC_SGA)],
            [InlineKeyboardButton("🏢 COORDENAÇÃO DE EXTENSÃO | COEX/SGA", callback_data=texto.COEX_SGA)],
        ]
    )


def menu_seac():

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠", callback_data=texto.HOME),
                InlineKeyboardButton("↩", callback_data=texto.ESTRUTURA_ADMINISTRATIVA),
                InlineKeyboardButton("📊", callback_data=texto.AVALIAR),
                InlineKeyboardButton("💬", callback_data=texto.SUGERIR),
            ],
            [
                InlineKeyboardButton("📞 Contatos e Canais", callback_data=texto.CONTATO_SEAC),
                InlineKeyboardButton("❓ Perguntas Frequentes", callback_data=texto.FAQ_SEAC),
            ],
        ]
    )


def menu_coex():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("🏠", callback_data=texto.HOME),
                InlineKeyboardButton("↩", callback_data=texto.ESTRUTURA_ADMINISTRATIVA),
            ],
            [
                InlineKeyboardButton("📞 Contatos e Canais", callback_data=texto.CONTATO_COEX),
                InlineKeyboardButton("❓ Perguntas Frequentes", callback_data=texto.FAQ_COEX),
            ],
        ]
    )


def faq_seac():
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "01 - Justificativa de Faltas/Reposição de Atividades❓",
                    callback_data="faq_seac1",
                )
            ],
            [InlineKeyboardButton("02 - Mudança de tuno/Turma❓", callback_data="faq_seac2")],
            [InlineKeyboardButton("03 - Aproveitamento de Estudos❓", callback_data="faq_seac3")],
            [InlineKeyboardButton("04 - Certificação de conhecimentos❓", callback_data="faq_seac4")],
            [InlineKeyboardButton("05 - Emissão de Diploma❓", callback_data="faq_seac5")],
            [InlineKeyboardButton("06 – Transferências❓", callback_data="faq_seac6")],
            [InlineKeyboardButton("07 – Renovação de Matrícula❓", callback_data="faq_seac7")],
            [InlineKeyboardButton("08 – Inscrição em Disciplina❓", callback_data="faq_seac8")],
            [InlineKeyboardButton("09 – Trancamento de Matrícula❓", callback_data="faq_seac9")],
            [InlineKeyboardButton("10 - Cancelamento de Disciplina❓", callback_data="faq_seac_10")],
            [
                InlineKeyboardButton("🏠", callback_data=texto.HOME),
                InlineKeyboardButton("↩", callback_data=texto.SEAC_SGA),
            ],
        ]
    )
