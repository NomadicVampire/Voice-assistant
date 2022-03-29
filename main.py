# 3 python library will be required namely: voice recognition, pyttsx3, pyaudio

from cgi import test
from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# listener, which will recognize our voice
listener = sr.Recognizer()
engine = pyttsx3.init() #this will talk to us

# converting voice into female voice
voices = engine.getProperty('voices')  #collecting all voices that python provides
engine.setProperty('voice',voices[1].id)  #changing voice audio

# function which can talk to us, which takes text as argunment of what we want to get listen
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone(device_index=2) as source:
            # here device index represents differnt mics in our PC
            print('Listening...')
            voice = listener.listen(source)
            # All we do here is to use microphone as source ṇand store it into voice variable            

            # now we will use google api which converts voice into text
            command = listener.recognize_google(voice)
            command = command.lower() #converting command in lower case

            # now if our command contains certain word then only it will execute
            if 'hello' in command:
                command = command.replace('hello', '') #this removes "hello" word from command
                print(command)

    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    
    # For playing song
    if 'play' in command:
        song = command.replace('play','')  #removes play word from command
        talk('playing'+song)
# --------------------
        # playing on youtube
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        # 
        talk('Current time is'+time)
    
    elif 'who is' in command:
        person = command.replace('who is','')
        info = wikipedia.summary(person,1)
        # Here 1 is no. of lines we want it as output from wikipidea
        print(info)
        talk(info)

    elif 'are you single' in command:
        talk('Sorry, i am in relationship with your router')

    elif 'joke' in command:
        talk(pyjokes.get_joke())    
        print(pyjokes.get_joke())    
    # return 0

    else:
        talk('Sorry, I cannot hear that')

while True:
    run_alexa()