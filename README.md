🎙️ Jarvis - Voice Assistant in Python

A simple voice-controlled personal assistant built using Python.
This assistant listens for the wake word "Jarvis" and performs tasks like opening websites, telling the time/date, and cracking jokes.

**Features**
Wake word detection ("Jarvis")
Opens:
Google
YouTube
GitHub
Instagram
Twitter
File Explorer
Tells current time
Tells today's date
Tells random jokes
Voice feedback using text-to-speech

**Technologies Used**
Python
SpeechRecognition
pyttsx3
Google Speech Recognition API
webbrowser module

**Installation**
1️⃣ Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2️⃣ Install dependencies
pip install SpeechRecognition pyttsx3 pyaudio

If pyaudio gives you problems on Windows (it usually does 🙄), install it using:
pip install pipwin
pipwin install pyaudio

▶️ How to Run
python your_script_name.py
After running:
Say "Jarvis"
Then give your command.
Example:
"Jarvis"
"Open YouTube"

**Platform Support**
Designed for Windows
Uses sapi5 speech engine (Windows only)

**License**
This project is open-source and free to use.
