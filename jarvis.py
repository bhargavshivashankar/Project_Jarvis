import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
# import subprocess


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
# print(voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("Good Morning!")

    elif hour >= 12 and hour<16:
        speak("Good Evening!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may i help you")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Please say again...")
        return "None"
    return query


if __name__ =="__main__":
    speak("Hello Bhargav.")
    wishme()
    
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
                
        elif 'open google' in query:
            webbrowser.open("google.com")

        # elif 'play music' in query:
        #     music_dir = 'file path'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open spotify' in query:
            os.startfile("C:\\Users\\bharg\\AppData\\Roaming\\Spotify\\Spotify.exe")
            # subprocess.Popen("C:\\Users\\bharg\\AppData\\Roaming\\Spotify")

        elif 'open firefox' in query:
            os.startfile("C:\Program Files\Mozilla Firefox\firefox.exe")

        elif 'anydesk' in query:
            os.startfile("C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        