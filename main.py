import speech_recognition as sr
import webbrowser
import pyttsx3 
import random

import pyttsx3

def speak(text):
    engine = pyttsx3.init("sapi5")  # create fresh engine every time
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # stop the engine to free resources

if __name__ == "__main__":
    speak("Initializing Jarvis, your personal assistant.") 
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word 'Hey Jarvis'...")

        while True:
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=2)
                command = r.recognize_google(audio).lower() 
                print(f"Recognized command: {command}")
                
                if "jarvis" in command:
                    responses = [
                        "How can I help you?",
                        "Yes, what can I do for you?",
                        "I'm listening.",
                        "How may I assist you?"
                    ]
                    print("Wake word detected. Awaiting command...")
                    speak(random.choice(responses))
                    print("Listening for command...")

                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio).lower()
                    print(f"Recognized command: {command}")
                    
                    if "open google" in command:
                        speak("Opening Google")
                        webbrowser.open("https://www.google.com")
                    elif "open youtube" in command:
                        speak("Opening YouTube")
                        webbrowser.open("https://www.youtube.com")
                    elif "open github" in command:
                        speak("Opening GitHub")
                        webbrowser.open("https://www.github.com")
                    elif "open file" in command:
                        speak("Opening File Explorer")
                        webbrowser.open("file:///C:/")  # Adjust path as needed
                    elif "what time is it" in command:
                        from datetime import datetime
                        now = datetime.now()
                        current_time = now.strftime("%H:%M")
                        speak(f"The current time is {current_time}")
                    elif "what's the date" in command:
                        from datetime import datetime
                        today = datetime.today()
                        current_date = today.strftime("%B %d, %Y")
                        speak(f"Today's date is {current_date}")
                    elif "tell me a joke" in command:
                        jokes = [
                            "Why don't scientists trust atoms? Because they make up everything!",
                            "Why did the scarecrow win an award? Because he was outstanding in his field!",
                            "Why don't programmers like nature? It has too many bugs.",
                            "Why do Java developers wear glasses? Because they don't see sharp."
                        ]
                        speak(random.choice(jokes))
                    elif "open insta" in command:
                        speak("Opening Instagram")
                        webbrowser.open("https://www.instagram.com")
                    elif "open twitter" in command:
                        speak("Opening Twitter")
                        webbrowser.open("https://www.twitter.com")
                    elif "exit" in command or "quit" in command:
                        speak("Goodbye!")
                        break

                    else:
                        speak("Sorry, I didn't understand that command.")
            except sr.WaitTimeoutError:
                speak("Listening timed out")
            except sr.UnknownValueError:
                speak("Could not understand audio")
            except sr.RequestError as e:
                speak(f"Could not request results; {e}")
