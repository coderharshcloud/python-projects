import pyttsx3
import wikipedia
import os
import datetime as dt
import speech_recognition as sr
import webbrowser


friday=pyttsx3.init("sapi5")
voices=friday.getProperty("voices")
friday.setProperty("voices",voices[0].id)

def wishme():
    hour=dt.datetime.now().hour
    if hour >=0 and hour <12:
        friday.say("good morning sir. please tell me how may i help you?")
        friday.runAndWait()

    if hour>=12 and hour<=14 :
        friday.say("good afternoon sir. please tell mehow may i help you?")
        friday.runAndWait()
    
    if hour>14 and hour<=20:
        friday.say("good evening sir. please tell me how may i help you?")
        friday.runAndWait()            





def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("recognizing...")
        query=r.recognize_google(audio,language="en-in")
        print(query)
        
    
    except Exception as e:
        print("sorry i did not get that.")
        return "none"
    return query    
    

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
            friday.say("searching wikiedia")
            friday.runAndWait()

            print("searching wikipedia")
            query=query.replace("wikipedia","")
            
            results=wikipedia.summary(query,sentences=5)
            print(results)
            
            friday.say("according to wikipedia")
            friday.runAndWait()
            
            friday.say(results)
            friday.runAndWait()

        if "open google" in query:
            webbrowser.open("google.com")
            friday.say("opening google")
            friday.runAndWait()
            print("opening google")
        
        if "open fiverr" in query:
            webbrowser.open("fiverr.com")
            friday.say("opening fiverr")
            friday.runAndWait()
            print("opening fiverr")

        if "open amazon" in query:
            webbrowser.open("amazon.com")
            friday.say("opening amazon")
            friday.runAndWait()
            print("opening amazon")

        

        if "open steam" in query:
            os.startfile("D:\\Steam\\steam.exe")
            friday.say("opening steam")
            friday.runAndWait()
            print("opening steam")

        if "open stack overflow" in query:
            friday.say("opening stackoverflow")
            friday.runAndWait()
            print("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        if "what is the time" in query:
            time=dt.datetime.now().strftime("%H:%M:%S")
            print(time)
            friday.say("sir it is currently")
            friday.runAndWait()
            print("sir it is curently")
            friday.say(time)
            friday.runAndWait()

        if "open command prompt" in query:
            os.system("start")

        if "shutdown" in query:
            friday.say("shutting down your pc")
            friday.runAndWait()
            print("shutting down your pc")
            #os.system("shutdown /s")

        #if "restart" or "reboot" in query:
            friday.say("rebooting your pc")
            friday.runAndWait()
            print("rebooting your pc")
            #os.system("shutdown /r")

        
             
        
        
        
    



          