# To start Jarvis AI file automatically on voice command, there should be another file, which should be running on background which opens and close file by recongnizing voice


import os
import speech_recognition as sr

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

while True:
    WakeUp = takecommand()
    
    if 'hello jarvis' in WakeUp:
        os.startfile("D:/Python/Jarvis/Jarvis.py")
    
    else:
        print("Error Occured")