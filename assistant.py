import pyttsx3  
import speech_recognition as sr  
import datetime 
import wikipedia 
import webbrowser
import smtplib  
import os  
import pyaudio 
import myMusic
import myscedule 


engine = pyttsx3.init()   
voices = engine.getProperty('voices') 

 
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()  


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am siri  Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tejas.katkade20@vit.edu', '12011102')
    server.sendmail('tejas.katkade20@vit.edu', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()   

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            myMusic.mysong()
           

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = r"C:\Users\Tejas Katkade\AppData\Local\Programs\Microsoft VS Code"
            os.startfile(codePath)
        elif 'my schedule' in query:
            myscedule.Myschedule()

        elif 'email to tejas' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tejas2002rk@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend ,I am not able to send this email")    
        elif 'stop siri' in query:
            break