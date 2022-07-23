import abc


class Cliente(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sendResposta(self, text, reply_markup):
        pass
