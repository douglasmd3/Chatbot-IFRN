from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# MENU 1
start_lines = [
    [InlineKeyboardButton("🏢 SETORES", callback_data="Estrutura_Administrativa"),]
]
start_lines = InlineKeyboardMarkup(start_lines)

# MENU 2: CHAMADA POR Estrutura_Administrativa OU MENU3 VOLTA MENU 2
setor_line = [
    # RETORNAR AO MENU 1
    [InlineKeyboardButton("🏠", callback_data="HOME")],
    [InlineKeyboardButton("🏢 SECRETARIA ACADÊMICA | SEAC/SGA", callback_data="SEAC/SGA")],
    [InlineKeyboardButton("🏢 COORDENAÇÃO DE EXTESÃO | COEX/SGA", callback_data="COEX/SGA")],
]
setor_line = InlineKeyboardMarkup(setor_line)

# MENU 3 - SEAC: CHAMADA POR SEAC/SGA OU COEX/SGA OU MENU4 VOLTA MENU 3
menu_seac = [
    # RETORNAR AO MENU 1 OU MENU 2
    [   InlineKeyboardButton("🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data="MENU2") ],
    [   InlineKeyboardButton("📞 Contatos e Canais", callback_data="Contato_seac"),
        InlineKeyboardButton("❓ Perguntas Frequentes", callback_data="FAQ_seac"),
    ],
            ]
menu_seac=InlineKeyboardMarkup(menu_seac)

# MENU 4 - CONTATO-SEAC: CHAMADA POR Contato_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3
contato_seac = [    [   InlineKeyboardButton("🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data="MENU3")   ]     ]
contato_seac = InlineKeyboardMarkup(contato_seac)

# MENU 4 - FAQ-SEAC: CHAMADA POR FAQ_seac + OPÇÕES DE VOLTAR INICIO OU MENU 4 PARA MENU 3
faq_seac = [
    [InlineKeyboardButton("🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data="MENU3") ],
    [InlineKeyboardButton("01 - Justificativa de Faltas/Reposição de Atividades❓", callback_data="faq_seac1")],
    [InlineKeyboardButton("02 - Mudança de tuno/Turma❓", callback_data="faq_seac2")],
    [InlineKeyboardButton("03 - Aproveitamento de Estudos❓", callback_data="faq_seac3")],
    [InlineKeyboardButton("04 - Certificação de conhecimentos❓", callback_data="faq_seac4")],
    [InlineKeyboardButton("05 - Emissão de Diploma❓", callback_data="faq_seac5")],
    [InlineKeyboardButton("06 – Transferências❓", callback_data="faq_seac6")],
    [InlineKeyboardButton("07 – Renovação de Matrícula❓", callback_data="faq_seac7")],
    [InlineKeyboardButton("08 – Inscrição em Disciplina❓", callback_data="faq_seac8")],
    [InlineKeyboardButton("09 – Trancamento de Matrícula❓", callback_data="faq_seac9")],
    [InlineKeyboardButton("10 - Cancelamento de Disciplina❓", callback_data="faq_seac10")],
    [InlineKeyboardButton("🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data="MENU3") ],
]
faq_seac=InlineKeyboardMarkup(faq_seac)

# MENU 5 - OP. FAQ-SEAC: CHAMADA POR OP. FAQ-SEAC + OPÇÕES DE VOLTAR INICIO OU MENU 5 PARA MENU 4
regressar_faq_seac = [
    [   InlineKeyboardButton("🏠", callback_data="HOME"), InlineKeyboardButton("↩", callback_data="MENU4")   ],
]
regressar_faq_seac = InlineKeyboardMarkup(regressar_faq_seac)




menu_coex = [
    [InlineKeyboardButton("🏠", callback_data="HOME"),InlineKeyboardButton("↩", callback_data="VOLTAR_SETOR_LINE")],
    [InlineKeyboardButton("📞 Contatos e Canais", callback_data="Contato_coex"),
    InlineKeyboardButton("❓ Perguntas Frequentes", callback_data="FAQ_coex")],
]
menu_coex=InlineKeyboardMarkup(menu_coex)