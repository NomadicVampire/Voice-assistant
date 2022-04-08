# JARVIS Voice Assistant
Python based voice assistant program 

A fully functioned python voice assistant which takes command from us and respond to it accordingly.

It requries numerous python libraries to run this python program namely :
<!-- Python libraries names -->
pyttsx3 - converts text to speech
speech_recognition - recognizes speech
webbrowser - used to open webpages
pywhatkit - used to send automatic whatsapp messages, play music from youtube
os - for opening file from device
wikipedia - used to search data from wiki 
pyautogui - Here, used for taking screenshot
keyboard - used to press any key on keyboard
pyjokes - collects jokes
pydictionary - used to find meaning, antonym, synonym for a given word
datetime - used to collecting current time, here used for alarm
playsound - here used to play sound at terminal


Hotward Detection - Here, we run another file(hotwardDetection.py) which run in background(another desktop) which is used to wake up our main file(Jarvis.py)


<!-- GUI -->
After making GUI from Qt designer, save it and add all used files in same folder.
Then convert this UI file into python file. Open cmd there, and type
=> pyuic5 -x filename.ui -o filename2.py
If it doesn't run then copy pyuic5 to this folder, then it will work