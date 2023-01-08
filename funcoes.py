from telegram import *
from telegram.ext import *
import logging, botoes, texto, time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
logger = logging.getLogger(__name__)

historico = []
lista_users = []
numeroUsuariosBotFileName="numeroUsuariosBot.txt"
numeroDeUsuarios=0

#Salva métricas com o numero de usuarios que já usou o bot. Essa funcao é chamada quando o usuario manda um /start
def salvarMetricaNumeroDeUsuarios(context):
    try:
        numeroDeUsuariosFile=open(numeroUsuariosBotFileName,'r')
    except FileNotFoundError:
        file=open(numeroUsuariosBotFileName,'x')
        numeroDeUsuariosFile=open(numeroUsuariosBotFileName,'r')

    numeroDeUsuarios=numeroDeUsuariosFile.read()
    numeroDeUsuariosFile.close()
    if(numeroDeUsuarios==''):
        numeroDeUsuarios=0
    else:
        numeroDeUsuarios=int(numeroDeUsuarios)

    context.bot.send_message(
        chat_id=-1001565692647, text=f"{numeroDeUsuarios+1}"  # -1001795732349
    )

    arquivo = open(numeroUsuariosBotFileName, "w")

    usuariosDoBot = str(numeroDeUsuarios+1)
    arquivo.write(usuariosDoBot)
    arquivo.close()

def start(update: Update, context: CallbackContext) -> None:
    historico.clear()

    salvarMetricaNumeroDeUsuarios(context)

    if update.effective_user:
        context.bot.send_photo(
        chat_id=update.effective_message.chat_id,
        photo=open('Imagens/Imagem-Inicial.jpg', 'rb'),
        caption=f'Olá, {update.effective_user.full_name}! que ótimo ter você por aqui 😀' # ERRO - em canal não é conhecido o username de usuário.
        )
        context.bot.send_message(
        chat_id=update.effective_message.chat_id,
        text=texto.start_texto,
        reply_markup=botoes.start_lines()
        )
       # register(     update, context)
    else: # Agendador ou não fazer nada no canal - somente adm podem interagir em canal;
        context.bot.send_message(
        # Soluçaõ seria quando em canal ou grupo, notificar a cada novo usuário ou interação específica e explicar regras do grupo.
        chat_id=update.effective_message.chat_id,
        # time para enviar a mensagem ou a cada N msgs enviar novamente se for em canal/grupo. [Díficil pois está filtrando tudo para realizar ação]
        text="Olá, conheçam a seção privada do chatbot @IFRN_SGA_BOT e vejam as possibilidades de atendimentos relativos ao campus IFRN/SGA. OBG 🤩"
        )
def sendResposta(handler, text, reply_markup):
    if text != "":
        handler.edit_message_text(
        text=text, reply_markup=reply_markup
        )
def responsehistorico(opcao):
    historico.append(opcao)
    return botoes.regressar_setor_line(historico)

def getReplyMarkup(option):
    replyMarkup = {
        texto.HOME: botoes.start_lines(),
        texto.ESTRUTURA_ADMINISTRATIVA: botoes.setor_line(),
        texto.SEAC_SGA: botoes.menu_seac(),
        texto.VOLTAR_FAQ_SEAC: botoes.faq_seac(),
        texto.CONTATO_SEAC: botoes.contato_seac(),
        # texto.CONTATO_SEAC: responsehistorico(texto.SEAC_SGA),
        texto.COEX_SGA: botoes.menu_coex(),
        texto.CONTATO_COEX: botoes.contato_coex(),
        texto.FAQ_SEAC: botoes.faq_seac(),
        # texto.FAQ_SEAC: responsehistorico(texto.SEAC_SGA),
        # **dict.fromkeys([texto.FAQSEAC1, "faq_seac2", "faq_seac3", "faq_seac4", "faq_seac5", "faq_seac6", "faq_seac7", "faq_seac8", "faq_seac9", "faq_seac10"], responsehistorico(texto.VOLTAR_FAQ_SEAC)),
        texto.FAQSEAC1: botoes.regressar_faq_seac(), "faq_seac2": botoes.regressar_faq_seac(), "faq_seac3": botoes.regressar_faq_seac(), "faq_seac4": botoes.regressar_faq_seac(), "faq_seac5": botoes.regressar_faq_seac(), "faq_seac6": botoes.regressar_faq_seac(), "faq_seac7": botoes.regressar_faq_seac(), "faq_seac8": botoes.regressar_faq_seac(), "faq_seac9": botoes.regressar_faq_seac(), "faq_seac10": botoes.regressar_faq_seac(),
        texto.FAQ_COEX: responsehistorico(texto.COEX_SGA)
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
    imprima = f'{update.effective_user.full_name} utilizou {query.data}'
    print(imprima)
    context.bot.send_message(
        chat_id=-1001565692647,text=imprima)

    #register(update, context)
def sugerir(update: Update, context: CallbackContext) -> None:
    context.bot.send_message(
    chat_id=update.effective_message.chat_id,
    text="Ok, A próxima mensagem que me enviar será armazenada no nosso canal de sugestões. A partir de Agora sinta-se livre para opnar, sua "
         "sugestão é fundamental para que possamos cada vez mais implementar melhorias e prestar - lhe  um melhor atendimento."
    )
    time.sleep(10)
    A = context.bot.forward_message(
        chat_id=-1001565692647, from_chat_id=update._effective_user.id,
        message_id=update.message.message_id + 2
    )
    print(A)
    # register(    update, context)


def register (update: Update, context: CallbackContext) -> None:
    # para interações diretas, registra e conta usuários e [interações] em canal no Telegram.
    # ERRO - o registro filtra as interações, se estiver em um canal não registra o username de usuário pois a interação é em canal(Em grupo ocorre o registro].
    #if not update.effective_user: # and novo usuário/Filters.command (pode ser soluçâo) # o grupo funciona como usuário direto. o canal tem uma interação constante.
        # se não [user], encaminhar ao bot direto; # ERRO - em canal são constantes msgs, como o register filtra as interações [filters.all], a recomendação para o bot é constante. pode ser chato.

    #else: # Referencia: # https://pt.stackoverflow.com/questions/431432/como-contar-elementos-repetidos-numa-lista-de-tuplos
          # https://cursos.alura.com.br/forum/topico-criar-uma-lista-com-os-itens-repetidos-157518#:~:text=Dá%20pra%20usar%20uma%20função,Bons%20estudos!
    lista_users.append(f'{update.effective_user.full_name}')
    lista_users_x = [t for t in lista_users]
    dicUsuario = {}
    for x in lista_users_x:
        dicUsuario[(x)] = lista_users_x.count(x)
    W = f"Usuários e Nºx que utilizou o BOT:\n{dicUsuario}\nTotal de interações: {len(lista_users)}\nTotal de usuários: {len(set(lista_users))}"
    context.bot.send_message(
    chat_id= -1001565692647, text=f"{W}" #-1001795732349
    )




        #context.bot.send_message(chat_id=update.effective_message.chat_id, text="Use /start ou /menu.")
    #[cp]context.bot.forwardMessage(chat_id=-1001565692647, from_chat_id=update.effective_message.chat_id, message_id=6784) - tentativa de registrar interações :O
    # ENVIAR MSG PARA INICIAR O BOT [HELP] OU NOME CAMINHO PARA O BOT.

def iniciar() -> None:

    token = "API"
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

    dispatcher.add_handler(
        CommandHandler("start", start)
    )
    dispatcher.add_handler(
        CommandHandler("sugerir", sugerir)
    )
    updater.dispatcher.add_handler(
        CallbackQueryHandler(balloon)
    )

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    iniciar()
