import pyttsx3

engine = pyttsx3.init()
name = input("What's ur name ? ")
engine.say(f"hello, {name}")
engine.runAndWait()