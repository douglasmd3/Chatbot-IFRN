import sys

import psycopg2 as MSCNT
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
        self.connect = MSCNT.connect(
            user="ardoqwcvwguqhl",
            password="d2d13e7cedc177e63bde1aea4373b11f12863282c0cef82eaf906251802d83f0",
            host="ec2-50-19-255-190.compute-1.amazonaws.com",
            database="d6ggk08ff8eilr",sslmode='require'
        )
        # self.connect = MSCNT.connect(
        #     user="qwzogpufdqemlg",
        #     password="bb46a9a5c70414469630f407b20c7d332c4b8da85b3e2983248fcaa292d065d5",
        #     host="ec2-44-206-197-71.compute-1.amazonaws.com",
        #     database="d2q6qddvn64d66",sslmode='require'
        # )
        return self.connect.cursor()

    def visualizar_sugestoes(self):
        lista_sugestao=[]
        self.cnt.execute('select * from sugestao')

        show = self.cnt.fetchall()
        for linha in show:
            lista_sugestao.append(f"NOME: {linha[0]},MENSAGEM: {linha[1]}")
        self.connect.commit()
        return lista_sugestao

    def gravar_sugestao(self,usuario, sugestao):
        try:
            self.cnt.execute(f"insert into sugestao (nome, mensagem) values ('{usuario}','{sugestao}')")
            self.connect.commit()
            print(self.visualizar_sugestoes()[-1])
            sys.stdout.flush()
            return True
        except:
            print("comentário não salvo.")
            return None

    def gravar_n_interacoes(self, n_interacoes):
        # no banco o Quser tem que iniciar com 0 e não estar vazio.
        self.cnt.execute(f"update interacao set quantidade_de_interacao = {n_interacoes}")
        self.connect.commit()

    def gravar_n_usuarios(self,n_usuarios):
        self.cnt.execute(f"update register set quantidade_de_usuario = {n_usuarios}")
        self.connect.commit()

    def gravar_avaliar_bom(self, bom):
        self.cnt.execute(f"update satisfacao set _bom_ = {bom}")
        self.connect.commit()

    def gravar_avaliar_ruim(self, ruim):
        self.cnt.execute(f"update satisfacao set _ruim_ = {ruim}")
        self.connect.commit()

    def gravar_avaliar_normal(self, normal):
        self.cnt.execute(f"update satisfacao set normal = {normal}")
        self.connect.commit()

        print()

    def __init__(self):
        self.cnt=self.criar_conexao()
