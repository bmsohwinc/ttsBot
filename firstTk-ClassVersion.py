from tkinter import *
import pyttsx3 

class Bot:
	
	def __init__(self, root, engine):
		self.engine = engine
		self.engine.say('Hi! I am your friend!. Please give me a name')
		self.engine.runAndWait()
		botName = input()
		self.engine.say('Thanks for such a wonderful name.')
		self.engine.say(str(botName + 'will, help you...'))
		#self.engine.say('I will try to repeat whatever you say. ')
		self.engine.say('Please proceed')
		self.engine.runAndWait()
		
		self.root = root
		
		self.voiceValue = IntVar()
		self.process()


	def DialogBox(self):
		dialog = Toplevel()
		dialog.geometry('100x100')

	def DialogMan(self, message):
		if message:
			self.engine.say(message)
			self.engine.runAndWait()
		
	def clear(self, e1):
		e1.delete(0, 'end')

	#def voiceSpeed(self, voiceVal):
		#value = Label(self.root, text=voiceVal)
		#value.grid(row=5, column=23)
		#self.engine.setProperty('rate', voiceVal)

	def voiceSpeed(self):
		print('In voiceSpeed funcs with speed = ', self.voiceValue.get())
		if not self.voiceValue.get():
			self.VoiceValue.set(30)		# = 30
		value = Label(self.root, text=str(self.voiceValue.get()))
		value.grid(row=5, column=23)
		self.engine.setProperty('rate', self.voiceValue.get())

	def showMe(self, msg):
		message = Message(root, text=msg)
		message.grid(row=5, column=10)
		message.config(bg='lightgreen')

	def byeBye(self):
		self.engine.say('Ok, Bye. Nice to talk to you!')
		self.engine.runAndWait()
		self.engine.stop()
		self.root.destroy()
		
	def process(self):
		l1 = Label(self.root, text='Your message')
		l1.grid(row=0)

		e1 = Entry(root)
		e1.grid(row=0, column=5)
		e1.bind('<Return>', (lambda event: self.DialogMan(e1.get())))
		e1.bind('<Escape>', (lambda event: self.clear(e1)))

		showButton = Button(self.root, bg='green', text='Repeat It', width=20, command=lambda: self.DialogMan(e1.get()))
		showButton.grid(row=5, column=0)
		
		clearButton = Button(self.root, bg='yellow', text='Clear It', width=20, command=lambda: self.clear(e1))
		clearButton.grid(row=10, column=0)		

		quitButton = Button(self.root, bg='red', text='Bye', width=20, command=lambda: self.byeBye())
		quitButton.grid(row=15, column=0)
		
		# Can use scale, but change wasn't effective
		#voiceRate = Scale(self.root, from_=20, to=150, orient=HORIZONTAL, command=lambda val: self.voiceSpeed(voiceRate.get()))
		#voiceRate.grid(row=20, column=10)
		
		rate1 = Radiobutton(self.root, text='10', variable = self.voiceValue, value=10, command=self.voiceSpeed)
		rate1.grid(row=20, column=0)
		rate1 = Radiobutton(self.root, text='1', variable = self.voiceValue, value=1, command=self.voiceSpeed)
		rate1.grid(row=22, column=0)
		rate1 = Radiobutton(self.root, text='2', variable = self.voiceValue, value=2, command=self.voiceSpeed)
		rate1.grid(row=24, column=0)
		rate1 = Radiobutton(self.root, text='340', variable = self.voiceValue, value=340, command=self.voiceSpeed)
		rate1.grid(row=26, column=0)
		rate1 = Radiobutton(self.root, text='450', variable = self.voiceValue, value=450, command=self.voiceSpeed)
		rate1.grid(row=28, column=0)
		rate1 = Radiobutton(self.root, text='560', variable = self.voiceValue, value=560, command=self.voiceSpeed)
		rate1.grid(row=30, column=0)
		rate1 = Radiobutton(self.root, text='6', variable = self.voiceValue, value=6, command=self.voiceSpeed)
		rate1.grid(row=32, column=0)
		rate1 = Radiobutton(self.root, text='50', variable = self.voiceValue, value=50, command=self.voiceSpeed)
		rate1.grid(row=34, column=0)
		rate1 = Radiobutton(self.root, text='120', variable = self.voiceValue, value=120, command=self.voiceSpeed)
		rate1.grid(row=36, column=0)
		rate1 = Radiobutton(self.root, text='150', variable = self.voiceValue, value=150, command=self.voiceSpeed)
		rate1.grid(row=38, column=0)
		rate1 = Radiobutton(self.root, text='180', variable = self.voiceValue, value=180, command=self.voiceSpeed)
		rate1.grid(row=40, column=0)

root = Tk()
root.geometry('400x300')

engine = pyttsx3.init()

newBot = Bot(root, engine)

root.mainloop()

engine.stop()
print("Things are normal now. !!")






'''
# To get the different voices 

voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hello World!")
    engine.runAndWait()
    engine.stop()

'''

'''
	Readables:
	
https://www.tutorialspoint.com/python/tk_radiobutton.htm
https://www.geeksforgeeks.org/radiobutton-in-tkinter-python/
https://stackoverflow.com/questions/54641750/python-typeerror-lambda-takes-0-positional-arguments-but-1-was-given-due-t
https://stackoverflow.com/questions/14508727/how-to-get-value-out-from-the-tkinter-slider-scale
https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter/16996475
https://stackoverflow.com/questions/32499491/python-text-to-speech-using-pyttsx
https://pythonprogramming.net/python-3-tkinter-basics-tutorial/

Awesome for OOP starting:
	https://www.digitalocean.com/community/tutorials/how-to-construct-classes-and-define-objects-in-python-3
	https://dzone.com/articles/python-class-attributes-vs-instance-attributes

'''
