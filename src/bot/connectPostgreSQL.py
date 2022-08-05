import psycopg2 as MSCNT
# https://www.youtube.com/watch?v=CrSLbdk6PqI

NUMERODEUSUARIOS = 0
# implementar o paramentro de start como uma função chamando as informações do banco.

# informação do database no heroku
def gravarMSG(receba_nome,receba_msg):
    connect = MSCNT.connect(
        user="ardoqwcvwguqhl",
        password="d2d13e7cedc177e63bde1aea4373b11f12863282c0cef82eaf906251802d83f0",
        host="ec2-50-19-255-190.compute-1.amazonaws.com",
        database="d6ggk08ff8eilr"
    )

    cnt = connect.cursor()
    cnt.execute(f"insert into sugestao (nome, mensagem) values ('{receba_nome}','{receba_msg}')")

    cnt.execute('select * from sugestao')

    show = cnt.fetchall()
    for linha in show:
        print(f"NOME: {linha[0]},MENSAGEM: {linha[1]}")

    connect.commit()
    connect.close()