# email = miniproject759@gmail.com
# password = ocln rrbd ozli ayps

import speech_recognition as sr
import pyttsx3
import smtplib
from email.message import EmailMessage
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/")
def login():
    return render_template("login.html")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            modified_text = modify_text(text)
            modified_text = ([word.lower() for word in modified_text.split()])
            whole_email = []
            for element in modified_text:
                whole_email.append(element)
            modified_text = ''.join(whole_email)
            print("You said:", modified_text)
            if "stop" in modified_text:
                stop_execution()
            return modified_text

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Say it again")
            return recognize_speech()
        except sr.RequestError as e:
            print("Error:", e)
            return recognize_speech()

def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully!")
        return True
    except Exception as e:
        print("Error:", e)
        return False

def main():
    speak("Welcome to voice-based email system.")
    # print("Welcome to voice-based email system.")

    # speak("What do you want to do speak or type?")
    # # print("What do you want to do speak or type?")

    # while True:
    #     choice = int(input("type 1.Speak or 2.Type: "))
    #     if choice == 1:
    #         continue;
    #     elif choice == 2:
    #         return type()
    #     else:
    #         speak("Invalid choice. Try again")
    #         break
    
    speak("Please say your email address or say 'stop' to exit")
    # print("Please say your email address or say 'stop' to exit")
    sender_email = recognize_speech()

    speak("Please say your email password.")
    # print("Please say your email password.")
    sender_password = recognize_speech()
    
    speak("Please say recipient's email address.")
    # print("Please say recipient's email address.")
    receiver_email = recognize_speech()
    
    speak("What is the subject of your email?")
    # print("What is the subject of your email?")
    subject = recognize_speech()
    
    speak("What is the message?")
    # print("What is the message?")
    body = recognize_speech()
    
    if sender_email and sender_password and receiver_email and subject and body:
        if send_email(sender_email, sender_password, receiver_email, subject, body):
            speak("Email sent successfully!")
            print("Email sent successfully!")
        else:
            speak("Failed to send email. Please try again.")
            print("Failed to send email. Please try again.")


def modify_text(text):
    modified_text = text.replace("at the rate", "@").replace("Dot com",".com").replace("dollar", "$").replace("spcae", " ")
    return modified_text

def stop_execution():
    print("Stopping...")
    raise SystemExit

# def type():
#     speak("Please type your email address or type 'stop' to exit")
#     sender_email = input("Enter your email address: ")

#     speak("Please say your email password.")
#     sender_password = input("Enter your email password: ")
    
#     speak("Please say recipient's email address.")
#     receiver_email = input("Enter receiver email address: ")
    
#     speak("What is the subject of your email?")
#     subject = input("Enter subject of mail: ")
    
#     speak("What is the message?")
#     body = input("Enter your message: ")

#     if sender_email and sender_password and receiver_email and subject and body:
#         if send_email(sender_email, sender_password, receiver_email, subject, body):
#             speak("Email sent successfully!")
#             print("Email sent successfully!")
#         else:
#             speak("Failed to send email. Please try again.")
#             print("Failed to send email. Please try again.")

@app.route("/login", methods=['POST'])
def verification(sender_email, sender_password):
    receiver_email = sender_email
    subject =  "Verification Email"
    body = "Email verified successfully"
    if sender_email and sender_password and receiver_email and subject and body:
        if send_email(sender_email, sender_password, receiver_email, subject, body):
            speak("Email sent successfully!")
            print("Email sent successfully!")
            return render_template("index.html")
        else:
            speak("Failed to send email. Please try again.")
            print("Failed to send email. Please try again.")
            return False

if __name__ == "__main__":
    # main()
    app.run(debug=True)