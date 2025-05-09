import sys
import pyttsx3  
import os  
import datetime  
import webbrowser  
import random  
import wikipedia  
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
from nltk import pos_tag
engine = pyttsx3.init()
def speak(voice):  
    engine.say(voice)  
    engine.runAndWait()
if len(sys.argv) < 2:
    print("No command provided.")
    sys.exit()
command = sys.argv[1].lower()
now = datetime.datetime.now()
try:
    if "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.bing.com/search?q={query}"
        speak(f"Searching for {query}")
        webbrowser.open(url)
        print(f"Bot: Searching for {query}")

    elif "open google" in command:
        speak("Opening Google Chrome.")
        os.system("open https://www.google.com")
        print("Bot: Opening Google Chrome.")

    elif "open notepad" in command:
        speak("Opening Notepad.")
        os.system("open -a TextEdit")
        print("Bot: Opening Notepad.")

    elif "current time" in command:
        current_time = f"{now.hour}:{now.minute}"
        speak(f"The current time is {current_time}")
        print(f"Bot: The current time is {current_time}")

    elif "today's date" in command:
        date_str = f"{now.day}/{now.month}/{now.year}"
        speak(f"Today's date is {date_str}")
        print(f"Bot: Today's date is {date_str}")

    elif "random number" in command:
        num = random.randint(1, 10)
        speak(f"The random number is {num}")
        print(f"Bot: The random number is {num}")

    else:
        tokens = word_tokenize(command)
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in tokens if w.lower() not in stop_words]
        tagged = pos_tag(filtered)
        keywords = [w for w, tag in tagged if tag.startswith("NN") or tag.startswith("NNS")]
        try:
            summary = wikipedia.summary(" ".join(keywords), sentences=2)
            speak(summary)
            print(summary)
        except Exception as e:
            speak("I could not find anything relevant.")
            print("Bot: I could not find anything relevant.")
except Exception as e:
    speak("An error occurred.")
    print(f"Error: {str(e)}")