import os
import wolframalpha
import wikipedia
from tkinter import *
import tkinter.messagebox
import speech_recognition as sr
import time
wn= Tk()
wn.geometry("700x600")
while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("speak something.... ")
		audio = r.listen(source)

		try:
			text = r.recognize_google(audio)
			if text == "stop":
				break
			else:
				print(text)
				answer= wikipedia.summary(text)

				label=Label(wn,text=answer,font="times 10 bold")
				label.pack()
				wn.after(5000000,lambda:wn.destroy())
				wn.mainloop()
		except:
			print("Sorry cannot hear you")