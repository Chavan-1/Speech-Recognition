
import pyttsx3                              # for speak function
import datetime                             # for date and time function
import speech_recognition as sr             # for speech recognition
import wikipedia
import smtplib as s                         # for sending mail function
import webbrowser as wb                     # for opening chrome
import os
import pyautogui                            # for screenshot function
import psutil                               # for cpu and battery usage function
import pyjokes                              # for joke functi

engine = pyttsx3.init()

def speak(audio):                  # speak function
    engine.say(audio)
    engine.runAndWait()

def time():                           # time function
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")      # text to speech
    speak(Time)

def date():                           # date function
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(year)
    speak(month)

def wishme():                                     # greeting and wishme function
    speak("Welcome back ma'am!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good morining ma'am")
    elif hour >= 12 and hour<18:
        speak("Good afternoon ma'am")
    elif hour >= 18 and hour<24:
        speak("Good evening ma'am")
    else:
        speak("Good night ma'am")
    speak("Jarvis at your service.Please tell me how can i help you ma'am")

def takecommand():                              # take command function speech recognition
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
         print("Recognizing...")
         query = r.recognize_google(audio, language="em-in")
         print(query)

    except Exception as e:
        print(e)
        speak("Say that again please")

        return "None"
    return query

def sendmail(to, content):                       # send mail
    server = s.SMTP('smtp.gmail.com', 587)                # (local host name, port no.)
    server.ehlo()
    server.starttls()                                     # to start encryption mode
    server.ehlo()
    server.login("SENDER_EMAIL_ID", "PWD")
    server.sendmail("EMAIL_ID", to, content)
    print("send successfully...")
    server.quit()

def screenshot():                                           # screenshot function
    img = pyautogui.screenshot()
    img.save("C:\\Users\\chavan aarti\\Pictures\\Camera Roll\\ss.png")

def cpu():                                                 # cpu and battery usage function
    cpu_usage = str(psutil.cpu_percent())
    speak("CPU is at"+ cpu_usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():                                         # jokes function
    speak(pyjokes.get_joke())

if __name__ == "__main__":                  # main function
    wishme()
    while True:
        query = takecommand().lower()
        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:                # wikipedia search
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = 'RECIEVER_EMAIL_ID'
                sendmail(to, content)
                speak(content)
            except Exception as e:
                print(e)
                speak("Unable to send email")

        elif 'search in chrome' in query:              # Chrome search
            speak("What should I search?")
            Chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takecommand().lower()
            wb.get(Chromepath).open_new_tab(search+'.com')
            print("opened.")

        elif 'logout' in query:                        # logout, shutdown, restart function
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'play song' in query:                       # play songs
            song_dir = "C:/Users/chavan aarti/Music"
            song = os.listdir(song_dir)
            os.startfile(os.path.join(song_dir, song[1]))

        elif 'remember that' in query:                 # remember function it create a .txt file and write the data
            speak("What should I remember?")
            data = takecommand()
            speak("you said to remember that"+data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:          # it read the data from .txt file
            remember = open('data.txt', 'r')
            speak("you said to remember that" +remember.read())

        elif 'screenshot' in query:                           # screenshot function
            screenshot()
            speak("Done!")

        elif 'cpu' in query:                           # it speak about cpu and battery usage
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("terminating the program..")
            quit()








