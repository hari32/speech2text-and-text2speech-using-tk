#import module from tkinter for UI
from tkinter import *
import os
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("py speech_recognizer.py")
    
def function2():
    
    os.system("py text2speech.py")

#stting title for the window
root.title("TEXT2SPEECH AND SPEECH2TEXT CONVERSION WITH TK")

#creating a text label
Label(root, text="T2S AND S2T",font=("times new roman",22),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="SPEECH2TEXT",font=("times new roman",15),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="TEXT2SPEECH",font=("times new roman",15),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
