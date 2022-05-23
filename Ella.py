import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as googleScrap
import webbrowser
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.setProperty("rate", 130)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        line = "\nGood Morning."

    elif 12 <= hour <= 18:
        line = "\nGood Afternoon."

    else:
        line = "\nGood Evening."
    line = line + "\nI'm Ella. What do you want me to do?"
    init_respond_after_reply_2(line)


def takeCommand():
    """It takes microphone input from the user and returns the output."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.energy_threshold = 8888
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        line = "\nPlease say that again.."
        init_respond_after_reply_2(line)
        return "None"
    return query

def init_respond_after_reply_1(word):
    print("Opening " + word + " for you")
    speak("Opening " + word + " for you")

def init_respond_after_reply_2(line):
    print(line)
    speak(line)

if __name__ == "__main__":
    # speak("Hey Karan!! How was your day?")
    wishMe()

    while True:
        query = takeCommand().lower()

        #Logic for executing tasks..
        # if 'wikipedia' in query:
        #     speak("Searching Wikipedia....")
        #     query = query.replace("wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     print("According to wikipedia, " + results)
        #     speak("According to wikipedia, " + results)
        
        if 'who are you' in query or 'what is your name' in query or 'introduce yourself' in query:
            if 'what is your name' in query:
                print("I'm Ella, you can set a nickname for me.")
                speak("I'm Ella, you can set a nickname for me.")
                continue
            print("I'm Ella, I'm here as your personal assistant. Come On tell me something...")
            speak("I'm Ella, I'm here as your personal assistant. Come On tell me something...")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            init_respond_after_reply_1("youtube")


        elif 'open google' in query:
            webbrowser.open("google.com")
            init_respond_after_reply_1("google")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            init_respond_after_reply_1("stackoverflow")

        elif 'tell me about' in query or 'tell me something about' in query:
            modified_query = query.replace("tell me", "")
            speak("Searching " + modified_query)
            search_query = query.replace(" ", "+")
            # pywhatkit.search(query)
            url = 'https://google.com/search?q=' + search_query
            webbrowser.open(url)
            result = googleScrap.summary(search_query, sentences=1)
            init_respond_after_reply_2(result)
            
            # result = webbrowser.open(url)

        elif 'play' in query:
            query.replace("play", "")
            # webbrowser.open("youtube.com/query")
            line = "Playing your request"
            init_respond_after_reply_2(line)
            pywhatkit.playonyt(query)

        elif 'mother f*****' in query or 'b****' in query or 'f***' in query or 'bastard' in query or 'bollocks' in query or 'suck my dick' in query:
            if 'suck my dick' in query:
                line = "Please don't talk to me that way, Let's learn to treat each other better."
                init_respond_after_reply_2(line)
                continue
            line = "I didn't expect this from you. I will tell your parents, you're using abusive words against me."
            init_respond_after_reply_2(line)

        elif 'enough for today' in query or 'enough talking' in query or 'quit' in query or 'shut up' in query or 'bye' in query or 'thank you' in query:
            speak("\nByee..")
            exit()