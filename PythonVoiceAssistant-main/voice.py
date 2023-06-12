import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            # print(data)
            return data
        except sr.UnknownValueError:
            print(" Not Understand ")

# voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_12.0"


def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[25].id)
    rate = engine.getProperty("rate")
    engine.setProperty('rate', 150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    try :
        data1 = sptext().lower()
    except:
        data1 = ''
    if data1 == "okay":
        while not sptext():
            data1 = sptext().lower()
            print(data1)
            if "name" in data1:
                name = "my name is goggle"
                speechtx(name)
            elif "old are you" in data1:
                age = "I am 2 years old"
                speechtx(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif 'web' in data1:
                webbrowser.open("https://www.azamatsalamatov.com/")
            elif 'joke' in data1:
                joke_1 = pyjokes.get_joke(language="en", category='neutral')
                print(joke_1)
                speechtx(joke_1)
            elif "song" in data1:
                webbrowser.open("https://www.youtube.com/watch?v=bkvzfJSw6sI&ab_channel=%D0%9C%D0%B8%D1%80%D0%B1%D0%B5%D0%BA%D0%90%D1%82%D0%B0%D0%B1%D0%B5%D0%BA%D0%BE%D0%B2")
            elif "exit" in data1:
                speechtx("Thank you")
                break
            else:
                webbrowser.open(data1)
    else:
        print("thanks")
        