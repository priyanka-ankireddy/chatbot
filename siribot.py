# importing libraries
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

#defining a name and trainer for a chatbot
bot=ChatBot('SIRI')
bot.set_trainer(ListTrainer)

#defining path
#iterating through the directory of files and train the bot
for files in os.listdir('C:/Users/User/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'):
    data=open('C:/Users/User/Downloads/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()
    bot.train(data)

while True:
    message=input('You:')
    if message.strip!='Bye' or message.strip!='bye':
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('ChatBot:It was nice talking to you!')
        break
    
    
    
    
