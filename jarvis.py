import pyttsx3
import datetime


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

if __name__ =="__main__":
    speak("Hello Bhargav.")
    wishme()
