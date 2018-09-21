from unicodedata import normalize
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pyodbc


def get_bd(src): #procura "src" no banco de dados
    print("selecionando no banco de dados...")



def professor_check(professor): #procura o professor no bd



def msg_clear(msgToClean):
    cleaning = normalize('NFKD', msgToClean).encode('ASCII', 'ignore').decode('ASCII')
    clean = ''
    valid = "abcdefghijklmnopqrstuvwxyz"
    for char in cleaning.lower():
        if char in valid:
            clean += char
    return clean


def call_the_real_bot(quest):
    bot = ChatBot('Test')

    dialogue = ['Olá, como posso ajudar?']

    bot.set_trainer(ListTrainer)

    bot.train(dialogue)

    bot_response = bot.get_response(quest)
    print("COPs:", bot_response)


def response(FQ, real_msg):

    if "ondeeaauladoprofessorfabio" == FQ or "ondeeaauladefabio" == FQ or "ondeeaauladefabiobarreto" == FQ or "ondeeaauladoprofessorfabiobarreto" == FQ or "aondeeaauladoprofessorfabiobarreto" == FQ or "aondeeaauladofabiobarreto" == FQ or "aondeeaauladoprofessorfabio" == FQ or "aondeeaauladefabio" == FQ or "aondeeaauladefabiobarreto" == FQ or "aondeeaauladofabiobarreto" == FQ:
        print("COPs:A aula do professor Fábio Barreto é no lab 7!")
    elif "cadeaaula" == FQ:
        print("COPs:Não tem aula hoje, idiota!")
    else:
        call_the_real_bot(real_msg)


if __name__ == '__main__':

    while True:
        msg = input("Você:")
        response(msg_clear(msg), msg)
