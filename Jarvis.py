from genericpath import exists
from turtle import exitonclick
from unicodedata import decimal
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os    #for playing songs from device
import wikipedia 
import pyautogui
import keyboard #used to press any key on keyboard

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
    with sr.Microphone() as source:
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

    # function to open different apps
    def OpenApps():
        Speak("Tell the name of application")
        appName = takecommand()

        # installed apps
        if 'chrome' in appName:
            os.startfile('C:/Program Files/Google/Chrome/Application/chrome.exe')
        elif 'brave' in appName:
            os.startfile('C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe')
        elif 'word' in appName:
            os.startfile('C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE')

        # web apps
        elif 'instagram' in appName:
            webbrowser.open('https://www.instagram.com')
        elif 'facebook' in appName:
            webbrowser.open('https://www.facebook.com')

        else:
            Speak('Given application name is not in list or PC')

    # function to close an App
    def CloseApps(query):
        if 'youtube' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")
        elif 'brave' in query:
            os.system("TASKKILL /F /im brave.exe")
        elif 'music player' in query:
            os.system("TASKKILL /F /im Groove Music.exe")
        elif 'jarvis' in query:
            Speak('Closing Jarvis AI...')
            exit()

        else:
            Speak('The given app is not opened')

    # function to automate youtube
    def YoutubeAuto(comm):
        if 'pause' in comm:
            keyboard.press('k')
        if 'play' in comm:
            keyboard.press('k')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'increase volume' in comm:
            keyboard.press('up')
        elif 'decrease volume' in comm:
            keyboard.press('down')

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
            query = query.replace("google","")
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
        elif 'song' in query:
            Music()
        
        # search from wikipedia
        elif 'wikipedia' in query:
            Speak('Searching on Wikipedia....')
            query = query.replace("search ","")
            query = query.replace(" on wikipedia","")
            wiki = wikipedia.summary(query,2)
            # here 2 represents that it will speak first two lines from result
            Speak(f"According to Wikipedia, {wiki}")

        # Taking screenshot and storing at local storage
        elif 'screenshot' in query:
            Speak('Ok Sir, By which name you want to save screeshot? ')
            SSname = takecommand()
            SSname = SSname + ".png"
            path = 'D:/PythonScreenshots/' + SSname

            # taking ss
            ss = pyautogui.screenshot()
            ss.save(path)
            os.startfile("D:/PythonScreenshots/")
            Speak('Screeshot saved')

        # open app
        elif 'open app' in query:
            OpenApps()

        # close app
        elif 'close' in query:
            query = query.replace("close ","")
            CloseApps(query)
        
        # youtube automation
        elif ' video' in query:
            query = query.replace(" video","")
            YoutubeAuto(query)

        else:
            Speak("Sorry, Your voice is not clear")
           
TaskExc()

         