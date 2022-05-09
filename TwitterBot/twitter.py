from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *
import time

class TwitterBot():
	def __init__(self, username,password):
		self.username=username
		self.password=password
		self.bot=webdriver.Chrome()
	def login(self):
		bot=self.bot
		bot.get('https://twitter.com/login')
		time.sleep(5)
		email=bot.find_element_by_name('session[username_or_email]')
		password=bot.find_element_by_name('session[password]')
		email.clear()
		password.clear()
		email.send_keys(self.username)
		password.send_keys(self.password)
		password.send_keys(Keys.RETURN)
		time.sleep(5)
	def like_tweet(self,entry3):
		bot=self.bot
		bot.get('https://twitter.com/search?q='+str(entry3)+'&src=typed_query')
		while True:
			bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
			time.sleep(2)
			pyautogui.click(pyautogui.locateCenterOnScreen('1.png'),duration=2)
			time.sleep(3)

def execute():
	log=TwitterBot(str(entry1.get()),str(entry2.get()))
	log.login()
	log.like_tweet(entry3.get())


window=Tk()
window.geometry("700x600")

emails=Label(window,text="enter your email here",font="times 24 bold")
emails.grid(row=0,column=0)
entry1=Entry(window)
entry1.grid(row=0,column=6)

password=Label(window,text="enter your password here",font="times 24 bold")
password.grid(row=2,column=0)
entry2=Entry(window)
entry2.grid(row=2,column=6)

hashtag=Label(window,text="enter your hashtag here",font="times 24 bold")
hashtag.grid(row=4,column=0)
entry3=Entry(window)
entry3.grid(row=4,column=6)

b1 = Button(window,text=" GO ", command=execute,width=32,bg="gray")
b1.grid(row=7,column=6)
window.mainloop()