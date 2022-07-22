import abc
from telegram.ClienteTelegram import ClienteTelegram


class Cliente(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sendResposta(self, text, reply_markup):
        pass


if __name__ == '__main__':
    clienteTelegram = ClienteTelegram()
    clienteTelegram.iniciar()
