from asyncio.log import logger
import sys

import mysql.connector as MSCNT
from app_logging import logger 


# import psycopg2 as MSCNT
class bd_singleton_meta(type):

    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class bd_singleton(metaclass=bd_singleton_meta):
    def criar_conexao(self):
        # banco de dados local
        connect = MSCNT.connect(
            user="chatbot",
            password="ch@tb0t@db", #TODO: Colocar credenciais no .env
            host="10.225.0.4",
            database="chatbot",
        )
        return connect

    def visualizar_sugestoes(self):
        try:
            lista_sugestao = []
            self.cnt.execute("select * from sugestao")

            show = self.cnt.cursor().fetchall()
            for linha in show:
                lista_sugestao.append(f"NOME: {linha[0]},MENSAGEM: {linha[1]}")
            self.cnt.commit()
            return lista_sugestao
        except Exception as e:
            logger.exception(e)


    def gravar_sugestao(self, usuario, sugestao):
        try:
            self.cnt.cursor().execute(f"insert into sugestao (nome, mensagem) values ('{usuario}','{sugestao}')")
            self.cnt.commit()
            print(self.visualizar_sugestoes()[-1])
            sys.stdout.flush()
            return True
        except:
            logging.exception("comentário não salvo.")
            return None

    def gravar_n_interacoes(self, n_interacoes):
        # no banco o Quser tem que iniciar com 0 e não estar vazio.
        self.cnt.cursor().execute(f"update interacao set quantidade_de_interacao = {n_interacoes}")
        self.cnt.commit()

    def gravar_n_usuarios(self, n_usuarios):
        try:
            self.cnt.cursor().execute(f"update register set quantidade_de_usuario = {n_usuarios}")
            self.cnt.commit()
        except (MSCNT.Error, MSCNT.Warning)  as e:
            logging.exception(e)
            

    def gravar_avaliar_bom(self, bom):
        try:
            print(f"AVALIACAO BOA {bom}")
            self.cnt.cursor().execute("update satisfacao set _bom_ = %(bom)s",{'bom':bom}) #TODO: Fazer todas as queries usando este tipo de composicao de string
            print(self.cnt.commit())
        except (MSCNT.Error, MSCNT.Warning) as e:
            logging.exception(e)

    def gravar_avaliar_ruim(self, ruim):
        try:
            self.cnt.cursor().execute(f"update satisfacao set _ruim_ = {ruim}")
            self.cnt.commit()
        except (MSCNT.Error, MSCNT.Warning) as e:
            logging.exception(e)

    def gravar_avaliar_normal(self, normal):
        try:
            self.cnt.cursor().execute(f"update satisfacao set normal = {normal}")
            self.cnt.commit()
        except (MSCNT.Error, MSCNT.Warning) as e:
            logging.exception(e)


    def __init__(self):
        self.cnt = self.criar_conexao()
        
