import speech_recognition as sr
import easyimap as e
import smtplib
import pyttsx3

username = "gamingbuddies2021@gmail.com"
password = "Reliance$321"

r = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(str):
    print(str)
    engine.say(str)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        str = "Speak now:"
        speak(str)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            str = "Sorry, I didn't get that."
            speak(str)

def sendmail():

    recepient = "aadityarevandkar@gmail.com"

    str = "Please speak body of mail"
    speak(str)
    mail = listen()

    str = "You have spoken the message"
    speak(str)
    speak(mail)

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(username, password)
    server.sendmail(username, recepient, mail)
    server.quit()

    str = "Email has been sent successfully!"
    speak(str)

str = "Welcome to voice email service"
speak(str)

while(1):
    str = "What do you want to do:"
    speak(str)

    str = "Speak SEND to send mail or EXIT to quit"
    speak(str)

    ch = listen()

    if(ch == 'send'):
        str = "You have chosen to send an email"
        speak(str)
        sendmail()
    elif (ch == 'exit'):
        str = "You have choosen to  exit from the program"
        speak(str)
        exit(1)
    else:
        str = "Invalid choice! Please try again."
        speak(str)
        speak(ch)

