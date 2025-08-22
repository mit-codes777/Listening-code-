import speech_recognition as sr
import webbrowser
import time
from time import ctime 

r = sr.Recognizer()


def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, i did not get that..')
        except sr.RequestError:
            print("sorry, my speech service is down..")
        return voice_data



def respond(voice_data):
    if 'what is your name' in voice_data:
        print("My name is alex")
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio("what do you want to search")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url) 
        print("Here is what I found for " + search)
    if 'find location' in voice_data:
        location = record_audio("Which location you want to find")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url) 
        print("Here is the location which you gave " + location)
    if 'you can leave' in voice_data:
        exit()


time.sleep(2)
print("How can i help you ..")
while True:
    voice_data = record_audio()
    respond(voice_data)

