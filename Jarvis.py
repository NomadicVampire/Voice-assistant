from genericpath import exists
from turtle import exitonclick
from unicodedata import decimal
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os    #for playing songs from device
# import wikipedia

Assistant = pyttsx3.init('sapi5')

# Collecting voices module
voices = Assistant.getProperty('voices')
Assistant.setProperty('voices',voices[0].id)

def Speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f": {audio}")  
    #whatever it speaks, it will print
    Assistant.runAndWait()

# this function takes voice as input and converts it into text and returns it
def takecommand():
    command = sr.Recognizer()  #Recognizes command
    with sr.Microphone(device_index=3) as source:
        print("Listening...")
        command.pause_threshold = 1   #To prevent it stuck at listening
        audio = command.listen(source)

        try:
            print('Recognizing.....')
            query = command.recognize_google(audio,language='en-in')   #uses google to convert audio into command
            
            print(f"You said : {query}")  
            #f-string
        
        except Exception as Error:
            return "none"

        return query.lower()


def TaskExc():

    # function to open music file from device
    def Music():

        Speak("Tell the name of song which you want to play")
        music = takecommand()
        # local file location
        musicLocation = 'C:/Users/sudha/Desktop/Desktop/songs/'+ music + ".mp3"

        # checking file exits or not
        Speak("Playing "+ music)
        if(os.path.exists(musicLocation)):
            os.startfile(musicLocation)
        
        else:
            # if file doesn't exists then it plays on yt
            pywhatkit.playonyt(music)

    while True:
        query = takecommand()

        # Different commands to run Jarvis
        if 'hello' in query:
            Speak("hello sir, I am Jarvis AI")
            Speak("how can i help you")

        elif 'how are you' in query:
            Speak("That's none of your buisness")

        # exits the Jarvis
        elif 'bye' in query:
            Speak("Bye Sir! See you soon")
            break

        # opens given url, which is of youtube
        elif 'youtube search' in query:
            Speak("This is what I found related to your search")
            query = query.replace("jarvis","")
            query = query.replace("youtube search","")
            web = 'https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)
        
        # Google search
        elif 'google' in query:
            Speak("This is what I found related to your search")
            query = query.replace("on google","")
            pywhatkit.search(query)
        
        # website search
        elif 'website' in query:
            Speak("This is what I found related to your search")
            query = query.replace("open ","")
            query = query.replace(" website","")
            web = 'https://www.'+query+'.com'
            webbrowser.open(web)
            Speak('Webpage launched')

        # launchs website by giving its name
        elif 'launch' in query:
            Speak("Tell me the name of website")
            webpage = takecommand()
            query = query.replace("launch","")
            web = "https://www."+webpage+".com"
            webbrowser.open(web)
            Speak('Done Sir!')

        # plays music from file location, if not found then play from youtube
        elif 'music' in query:
            Music()
        
        # elif 'wikipedia' in query:

        else:
            Speak("Sorry, Your voice is not clear")
           
TaskExc()

        