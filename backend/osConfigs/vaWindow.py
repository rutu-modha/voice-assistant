import sys
import os  
import datetime  
import webbrowser  
import random  
import wikipedia  
from nltk.tokenize import word_tokenize  
from nltk.corpus import stopwords  
from nltk import pos_tag
if len(sys.argv) < 2:
    print("No command provided.")
    sys.exit()
command = sys.argv[1].lower()
now = datetime.datetime.now()
try:
    if "open microsoft edge" in command:
        ("Opening Microsoft Edge.")
        os.system("start msedge")
        print("Opened Microsoft Edge.")

    elif "search" in command:
        query = command.replace("search", "").strip()
        url = f"https://www.bing.com/search?q={query}"
        (f"Searching for {query}")
        webbrowser.open(url)
        print(f"Searching Bing for {query}")

    elif "open google" in command:
        ("Opening Google Chrome.")
        os.system("start chrome")
        print("Opened Chrome.")

    elif "open notepad" in command:
        ("Opening Notepad.")
        os.system("notepad")
        print("Opened Notepad.")

    elif "current time" in command:
        current_time = f"{now.hour}:{now.minute}"
        (f"The time is {current_time}")
        print(f"Current time: {current_time}")

    elif "today's date" in command:
        date_str = f"{now.day}/{now.month}/{now.year}"
        (f"Today's date is {date_str}")
        print(f"Today's date: {date_str}")

    elif "random number" in command:
        num = random.randint(1, 10)
        (f"The random number is {num}")
        print(f"Random number: {num}")

    else:
        tokens = word_tokenize(command)
        stop_words = set(stopwords.words('english'))
        filtered = [w for w in tokens if w.lower() not in stop_words]
        tagged = pos_tag(filtered)
        keywords = [w for w, tag in tagged if tag.startswith("NN")]
        try:
            summary = wikipedia.summary(' '.join(keywords), sentences=2)
            (summary)
            print(summary)
        except Exception as e:
            ("I could not find anything relevant.")
            print("Bot: I could not find anything relevant.")
except Exception as e:
    ("An error occurred.")
    print(f"Error: {str(e)}")