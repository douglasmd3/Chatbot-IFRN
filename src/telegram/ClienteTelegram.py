import sys
import os

#usando estas duas linhas para poder importar Cliente da pasta acima
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

import Cliente
import botoesTelegram
import texto
# import gtts
import logging
from telegram import ReplyMarkup, Update
from telegram.ext import CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler

historico = []
numeroUsuariosBotFileName="numeroUsuariosBot.txt"
numeroDeUsuarios=0
class ClienteTelegram(Cliente.Cliente):

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    #Salva métricas com o numero de usuarios que já usou o bot. Essa funcao é chamada quando o usuario manda um /start
    def salvarMetricaNumeroDeUsuarios(self,context):
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

    def start(self, update: Update, context: CallbackContext) -> None:
        historico.clear()
        self.salvarMetricaNumeroDeUsuarios(context)
        context.bot.send_photo(
            chat_id=update.effective_message.chat_id,
            photo=open('Imagens/Imagem-Inicial.jpg', 'rb'),
            caption=f'Olá, {update.effective_user.full_name}! que ótimo ter você por aqui 😀'
        )
        context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=texto.start_texto,
            reply_markup=botoesTelegram.start_lines()
        )

    def sendResposta(self,text,reply_markup):
        if text != "":
            self.handler.edit_message_text(text=text, reply_markup=reply_markup)
    

    
        


    def responsehistorico(self,opcao):
        historico.append(opcao)
        return botoesTelegram.regressar_setor_line(historico)

    def getReplyMarkup(self,option):
        replyMarkup = {
            texto.HOME: botoesTelegram.start_lines(),
            texto.ESTRUTURA_ADMINISTRATIVA: botoesTelegram.setor_line(),
            texto.SEAC_SGA: botoesTelegram.menu_seac(),
            texto.VOLTAR_FAQ_SEAC: botoesTelegram.faq_seac(),
            texto.CONTATO_SEAC: botoesTelegram.contato_seac(),
            # texto.CONTATO_SEAC: responsehistorico(texto.SEAC_SGA),
            texto.COEX_SGA: botoesTelegram.menu_coex(),
            texto.CONTATO_COEX: botoesTelegram.contato_coex(),
            texto.FAQ_SEAC: botoesTelegram.faq_seac(),
            # texto.FAQ_SEAC: responsehistorico(texto.SEAC_SGA),
            # **dict.fromkeys([texto.FAQSEAC1, "faq_seac2", "faq_seac3", "faq_seac4", "faq_seac5", "faq_seac6", "faq_seac7", "faq_seac8", "faq_seac9", "faq_seac10"], responsehistorico(texto.VOLTAR_FAQ_SEAC)),
            texto.FAQSEAC1: botoesTelegram.regressar_faq_seac(), "faq_seac2": botoesTelegram.regressar_faq_seac(), "faq_seac3": botoesTelegram.regressar_faq_seac(), "faq_seac4": botoesTelegram.regressar_faq_seac(), "faq_seac5": botoesTelegram.regressar_faq_seac(), "faq_seac6": botoesTelegram.regressar_faq_seac(), "faq_seac7": botoesTelegram.regressar_faq_seac(), "faq_seac8": botoesTelegram.regressar_faq_seac(), "faq_seac9": botoesTelegram.regressar_faq_seac(), "faq_seac10": botoesTelegram.regressar_faq_seac(),
            texto.FAQ_COEX: self.responsehistorico(texto.COEX_SGA)
        }
        

        return replyMarkup.get(option)


    def getResponseText(self,option, update):
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


    def getResponseTextReplyMarkup(self,option, update):
        return [self.getResponseText(option, update), self.getReplyMarkup(option)]


    def balloon(self,update: Update, context: CallbackContext) -> None:

        query = update.callback_query
        self.handler = query
        self.handler.answer()

        argumentos = self.getResponseTextReplyMarkup(query.data, update)
        self.sendResposta(argumentos[0], argumentos[1])


    # registro dos botões utilizados por usuário.
        print(f'{update.effective_user.full_name} utilizou {query.data}')


    def iniciar(self) -> None:
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
        dispatcher.add_handler(MessageHandler(Filters.all, self.start))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.balloon))

        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    clienteTelegram= ClienteTelegram()
    clienteTelegram.iniciar()
