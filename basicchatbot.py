import nltk
from nltk.chat.util import Chat, reflections
pairs =[
    (r'Hello|Hi',['Hello,how are you today']),
    (r'i am fine',['Glad to know that , how can i help you']),
    (r'what do you call yourself?',['I am just a simple chatbot']),
    (r'(.*)your name?',['My name is friday']),
    (r'(.*)age?',['I am just a computer program, i do not have age']),
    (r'Thanks',['You are welcome']),
    (r'Exit',['It was great please chatting with you , please visit again'])
    ]
#print(reflections)
print("welcome to friday chatbot")
chatbot=Chat(pairs)
chatbot.converse()

