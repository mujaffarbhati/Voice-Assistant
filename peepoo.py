import pyttsx3 
import speech_recognition as sr 
import wikipedia
import webbrowser
import datetime
import os
import pywhatkit
import requests
import bs4 as bs
import json
import pyjokes
import time

print("Whom would you like your assistant to be today (Type in the number):")
ass=input('''1. Peepoo\n2. Kikyo\n   Your Option:- ''')
if ass=="1":
    vass="Peepoo"
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
elif ass=="2":
    vass="Kikyo"
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
else:
    vass="Peepoo"
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    print("Default Assistant chosen")
   
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(f"Hello! I am {vass}. How can I assist you?")
    if hour>=0 and hour<12:
        speak("Hello! Good Morning!")

    elif hour>=12 and hour<18:
        speak("Hello! Good Afternoon!")   

    else:
        speak("Hello! Good Evening!")  

    speak(f"I am {vass}. How may i help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{vass} is Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Care to repeat again.....")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        if 'who are you' in query:
            speak(f"I am {vass}. A very awesome assistant. You can search wikipedia, google, youtube, etc. You can also use me to find the date and time along with current temperature of the region. You can also use me to play random musics to cheer up your mind. If you are bored I will share with you a joke or can help you send whatsapp messages. Feel free to call {vass} for your aid")

        elif 'hello' in query:
            speak("Hello Dude!Hope You had a wonderful day")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            query = query.replace("peepo", "")
            query = query.replace("kikyo", "")
            query = query.replace("search", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search google' in query:
            import wikipedia as googleScrap
            query = query.replace("for","")
            query = query.replace("search google" , "")
            query = query.replace("peepo", "")
            query = query.replace("kikyo", "")
            speak("This is what I found in my search")
            try:
                pywhatkit.search(query)
                result=googleScrap.summary(query,1)
                speak(result)
            except:
                print("Couldn't find releveant information")
            
        elif 'search youtube' in query:
            speak("This is what i found in my search")
            query = query.replace("peepo", "")
            query = query.replace("kikyo", "")
            query = query.replace("for", "")
            query = query.replace("search youtube", "")
            web="https://www.youtube.com/results?search_query="+query
            webbrowser.open(web)
            pywhatkit.playonyt(query)
            speak("Command Executed!")
        
        elif 'news' in query:
            api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=859f9c81379943b98270aa047049078d",
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=859f9c81379943b98270aa047049078d",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=859f9c81379943b98270aa047049078d",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=859f9c81379943b98270aa047049078d",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=859f9c81379943b98270aa047049078d",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=859f9c81379943b98270aa047049078d"}
            content = None
            url = None
            speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
            field = input("Type field news that you want: ")
            for key ,value in api_dict.items():
                if key.lower() in field.lower():
                    url = value
                    print(url)
                    print("url was found")
                    break
                else:
                    url = True
            if url is True:
                print("url not found")

            news = requests.get(url).text
            news = json.loads(news)
            speak("Here is the first news.")

            arts = news["articles"]
            for articles in arts :
                article = articles["title"]
                print(article)
                speak(article)
                news_url = articles["url"]
                print(f"For more information regarding it please visit: {news_url}")

                a = input("Press 1 to continue reading or else 2 to exit hearing news")
                if str(a) == "1":
                    pass
                elif str(a) == "2":
                    break
                speak("Thats all for today. Have a good day")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")   

        elif "direct message" in query:
            print("Note: Logs won't be kept for direct messages.")
            speak("Enter The phone Number")
            pn=int(input("Enter A Phone Number. Add The country Code In front (Avoid adding'+'):- "))
            speak("Enter text")
            msg=input("Text Message:- ")
            speak("Message is being sent. Have a check for the details on the whatsapp app.")
            print("Check For details on the whatsapp web")
            print("Directing....")
            time.sleep(2)
            webbrowser.open(f"https://web.whatsapp.com/send?phone=+{pn}&text={msg}")

        elif 'send message' in query:
            speak(f"Logs will be saved. Press 1 to proceed")
            a=input("Type in 1 to send the message to a phone number.")
            hour=int(datetime.datetime.now().strftime("%H"))
            time=int((datetime.datetime.now()+datetime.timedelta(minutes=2)).strftime("%M"))
            if a=="1":
                speak("Enter the Phone Number along with the country code ")
                P_No=input("Enter the phone number (Avoid writing '+')")
                if P_No.isnumeric():
                    speak("Type in the message! ")
                    msg=input("What message would you like to send: ")
                    pywhatkit.sendwhatmsg("+"+P_No,msg,hour,time)
                else :
                    print("Invalid number")
                    speak("Enter a correct valid number")
            else: 
                speak("Innvalid command")
                print("invalid command")
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\Asus\\Documents\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Its {strTime} dude")

        elif 'open code' in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif 'open calculator' in query:
            codePath ="C:\\Windows\\System32\\calc.exe"
            os.startfile(codePath)

        elif 'open downloads' in query:
            codePath="C:\\Users\\Asus\\Downloads"
            os.startfile(codePath)

        elif 'joke' in query:
            joke=pyjokes.pyjokes.get_joke(language="en",category="neutral")
            speak("Alright here I got one...")
            print(joke)
            speak(joke)
            speak("haha!! Funny isnt it")

        elif 'temperature' in query:
            search="Temperature"
            url=f"https://www.google.com/search?q="+search
            r=requests.get(url)
            data=bs.BeautifulSoup(r.text,"html.parser")
            temp=data.find("div", class_ ="BNeawe").text
            speak(f"current {search} is {temp}")
    
        elif 'thanks' in query:
            speak("You are very welcome!")
            speak("Any other help from me? ")
            test=input("Any other help to assist? ")
            if test=="no" or test=="No"or test=="nO" or test=="NO":
                speak("Alright have a good day")
                exit()
            else:
                pass

        
        elif 'sorry' in query:
            speak("No problem! You need not be")
        

        elif 'go to sleep' in query:
            a=print(f"{vass} is now gonna go to sleep")
            speak(f"{vass} is now gonna go to sleep")
            exit()

        elif "log off" in query:
            speak("Are you sure you want to logoff Sir!")
            logoff= input("Are You sure you want to log off.(Type YES in capitals for proceeding)")
            if logoff == "YES":
                   os.system("shutdown -l")
            else :
                 speak("Alright We are back in business")

        elif "switch off" in query: 
            speak("Are You sure you want to shutdown")
            shutdown = input("Do you wish to shutdown your computer? (Type YES in capitals for proceeding)")
            if shutdown == "YES":
                os.system("shutdown /s /t 1")
            else:
                break
        