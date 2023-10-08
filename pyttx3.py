import pyttsx3

def onStart():
    print('starting')

def onWord(name, location, length):
    print('word', name, location, length)

def onEnd(name, completed):
    print('finishing', name, completed)

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)

sen = 'Hi, my name is vasu and im using pyttsx3 library to run this program. Actully pyttx3 is python library to make a pre-define voice'


engine.say(sen)
engine.runAndWait()