import speech_recognition as sr
import pyaudio
import os
import pyttsx3


r=sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty('voice',engine.getProperty('voices')[1].id)  

def mysong():
      engine.say('which song do u want to play')
      engine.runAndWait()
      with sr.Microphone() as source:
             try:
                  print('give song name')
                  command=r.listen(source)
                  print('wait')
                  query = r.recognize_google(command)     
                  music=os.listdir('C:\python\mymusic')
             except FileNotFoundError as e:
                 print(f'error:{e}')
             except sr.UnknownValueError as e:
                  print(f'cant recognize again try')    
             except:
                 print('unexpected error')    
             else:
                
                 for i in music:
                       if query.title() in i:
                           os.startfile(os.path.join('C:\python\mymusic',i))
                           