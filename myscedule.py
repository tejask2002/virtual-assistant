import pyttsx3  
import speech_recognition as sr  
import datetime as d


timetable=['DMS theory','DMS lab','DMS tutorial','toc theory', 'toc lab','toc tutorial','data structure theory','data stucture lab','data structure tutorial',
'SE theory','SE lab','SE tutorial','EDI lab','SDP lab']
engine = pyttsx3.init()   
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Myschedule():
    if(d.date.today().weekday()==6):
        speak("today is sunday ,your day is off")
    elif(d.date.today().weekday()==0):
        monday()  
    elif(d.date.today().weekday()==1):
        tuesday()      
    elif(d.date.today().weekday()==2):
        wednesday() 
    elif(d.date.today().weekday()==3):
        thursday() 
    elif(d.date.today().weekday()==4):
        friday() 
    elif(d.date.today().weekday()==5):
        saturday()         

#Myschedule()

def gettime():
    time=d.datetime.now()
    return time.hour
 
  
def monday():
    
    if(gettime()==8):
         speak(f'you  have {timetable[6]} lecture now')
    elif(gettime()==9):
        speak(f'you  have {timetable[3]} lecture now')
    elif(gettime()==10):
        speak(f'you  have {timetable[0]} lecture now')
    elif(gettime()==12):
        speak(f'you  have {timetable[9]} lecture now') 
    elif(gettime()==16):
        speak(f'you  have {timetable[8]} lecture now')   
    else:
        speak('for now you are free dear')               
  
def tuesday():
    
    if(gettime()==8):
         speak(f'you  have {timetable[6]} lecture now')
    elif(gettime()==9):
        speak(f'you  have {timetable[3]} lecture now')
    elif(gettime()==10):
        speak(f'you  have {timetable[0]} lecture now')
    elif(gettime()==12):
        speak(f'you  have {timetable[9]} lecture now') 
    elif(gettime()==16):
        speak(f'you  have {timetable[2]} lecture now')   
    else:
        speak('for now you are free dear')   

def wednesday():
    
    if(gettime()==8):
         speak(f'you  have {timetable[6]} lecture now')
    elif(gettime()==9):
        speak(f'you  have {timetable[3]} lecture now')
    elif(gettime()==10):
        speak(f'you  have {timetable[0]} lecture now')
    elif(gettime()==12):
        speak(f'you  have {timetable[9]} lecture now') 
    elif(gettime()==16):
        speak(f'you  have {timetable[5]} lecture now')   
    else:
        speak('for now you are free dear')                        
       
def thursday():
    
    if(gettime()==12 or gettime()==13):
         speak(f'you  have {timetable[10]} lecture now')
    elif(gettime()==14 or gettime()==15):
        speak(f'you  have {timetable[4]} lecture now')
    else:
        speak('for now you are free dear') 
def friday():
    
    if(gettime()==12 or gettime()==13):
         speak(f'you  have {timetable[1]} lecture now')
    elif(gettime()==14 or gettime()==15):
        speak(f'you  have {timetable[7]} lecture now')
    else:
        speak('for now you are free dear') 
def saturday():
    
    if(gettime()==14 or gettime()==15):
         speak(f'you  have {timetable[13]} lecture now')
    elif(gettime()==16 or gettime()==17):
        speak(f'you  have {timetable[12]} lecture now')
    else:
        speak('for now you are free dear')            
