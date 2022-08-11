"""Funcao principal"""
from bot.telegram.ClienteTelegram import ClienteTelegram

if __name__ == "__main__":
    clienteTelegram = ClienteTelegram()
    clienteTelegram.iniciar()
# git push heroku main + heroku ps:scale worker=1 repete esse comando e testar sugerir;