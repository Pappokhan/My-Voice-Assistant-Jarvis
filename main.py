import webbrowser
import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def open_website(url, name):
    try:
        webbrowser.open(url)
        speak(f"Opening {name} for you...")
    except Exception as e:
        speak(f"Sorry, I couldn't open {name}. Error: {str(e)}")

def process_command(command, user_profile):
    command = command.lower()
    if "jarvis play music" in command:
        open_website("https://www.youtube.com/watch?v=ANzYzZOQOLk&t=18s", "Your music..")
    elif "jarvis open google" in command:
        open_website("https://www.google.com/", "Google..")
    elif "jarvis open youtube" in command:
        open_website("https://www.youtube.com/", "YouTube..")
    elif "jarvis open facebook" in command:
        open_website("https://www.facebook.com/", "Facebook..")
    elif "jarvis tell weather" in command:
        open_website("https://www.msn.com/en-xl/weather/forecast/in-Dhaka,Bangladesh?loc=eyJhIjoiVXR0YXJhIFN1aXRlIEF0IERoYWthIiwibCI6IkRoYWthIiwiYyI6IkJhbmdsYWRlc2giLCJpIjoiQkQiLCJnIjoiZW4teGwiLCJ4IjoiOTAuMzg4OCIsInkiOiIyMy44NjY0In0%3D&weadegreetype=C&ocid=msedgdhp&cvid=a444330bfd3d49e693e1b5e754c566c2", "Weather..")
    elif "what's my name" in command:
        if user_profile.get("name"):
            speak(f"Your name is {user_profile['name']}.")
        else:
            speak("I don't know your name. Please tell me your name.")
            user_name = listen()
            user_profile["name"] = user_name
            speak(f"Thank you, {user_name}. I'll remember your name.")
    elif "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don't understand your command.")


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return ""

if __name__ == "__main__":
    user_profile = {}

    speak("Hello, I am jarvis. How can I help you sir?")

    while True:
        command = listen()

        if command:
            process_command(command, user_profile)
