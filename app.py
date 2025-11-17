import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

r = sr.Recognizer()
phone_numbers = {"ravi": "+91 1234567890", "swaroop": "+91 9876543210", "suresh": "+91 1122334455"}
bank_account_numbers = {"tt": "12345674444", "sb": "0987654321", "rr": "1122334455"}

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Change index to select different voice
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening...Ask now...")
            audioin = r.listen(source)
            my_text = r.recognize_google(audioin)
            my_text = my_text.lower()
            print(my_text)


            # ask to play a song
            if 'play' in my_text:
                my_text = my_text.replace('play', '')
                speak('Playing ' + my_text)
                pywhatkit.playonyt(my_text)
            
            # ask date
            elif 'date' in my_text:
                today = datetime.date.today()
                speak("Today's date is " + str(today))
            
            # ask time
            elif 'time' in my_text:
                timenow = datetime.datetime.now().strftime('%H:%M')
                speak(timenow)


            # ask details about any person
            elif 'who is' in my_text or 'what is' in my_text or 'when' in my_text or 'tell me about' in my_text:
                topic = my_text.replace('who is', '').replace('what is', '').replace('when', '').replace('tell me about', '').strip()
                try:
                    info = wikipedia.summary(topic, sentences=2)
                    print("Answer:", info)
                    speak(info)
                except wikipedia.exceptions.DisambiguationError:
                    speak("There are multiple results. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("I couldn't find any information on that topic.")


            # ask phone numbers
            elif 'phone number' in my_text:
                names = list(phone_numbers)
                print(names)
                for name in names:
                    if name in my_text:
                        print(name + " phone number is " + phone_numbers[name])
                        speak(name + " phone number is " + phone_numbers[name])

            # asl personal bank account numbers
            elif 'bank account' in my_text:
                banks = list(bank_account_numbers)
                for bank in banks:
                    if bank in my_text:
                        print(bank + " bank account number is " + bank_account_numbers[bank])
                        speak(bank + " bank account number is " + bank_account_numbers[bank])

            # if not recognized
            else:
                speak("Sorry, I didn't understand that. Please try again.")
    except:
        print('Error in capturing microphone....')
while True:
    commands()


