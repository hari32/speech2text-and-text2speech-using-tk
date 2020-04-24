from gtts import gTTS
import os

eng = input("write something and press enter:")
#eng = "hai welcome ,everyone to this channel please subscribe"

print(eng)

obj = gTTS(text = eng)

obj.save('eng.mp3')

print("files saved sucessfully")

os.system("start eng.mp3")



 
