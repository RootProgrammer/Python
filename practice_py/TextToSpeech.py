from gtts import gTTS
from playsound import playsound

if __name__=="__main__":
    name=input("Enter Your Name: ")
    text = "Hello "+name+", Welcome to Google Text To Speech."

    obj = gTTS(text=text, lang="en", slow=False)
    obj.save("welcome.mp3")

    playsound(".\welcome.mp3")
