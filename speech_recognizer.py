import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)

try:
    print(audio)

except:
    print("your voice not recogined")
