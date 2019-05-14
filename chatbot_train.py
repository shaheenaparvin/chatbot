from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import os

bot = ChatBot('bot')
#bot.set_trainers(ListTrainer)

bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")




  
for files in os.listdir('C:/Users/de\Desktop/chatterbot_corpus/english/'):
        data = open('C:/Users/de\Desktop/chatterbot_corpus/english/' + files,'r').readlines()
        bot.train(data)



while True:
        message = input('You : ')
        if message.strip() != 'Bye':
                reply = bot.get_response(message)
                print('chatbot : ',reply)
        if message.strip() == 'Bye':
                print('chatbot : Bye ')
                break
