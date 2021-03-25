from tkinter import *
from tkinter import filedialog
import subprocess
import os

class IDE:
	def __init__(self):
		self.test = ""
		self.pathFile = ""
		self.fileName = ""
		self.menuBar = ""
		self.screenHeight = 0
		self.screenWidth = 0

		self.UserName = self.currentUser()
		# userPath = "C:/Users/" + UserName
		self.userPath = "C:/Progra/Python/PyIDE"

		self.window = Tk()
		self.window.state('zoomed')
		self.window.title("IDE Python")
		self.window.configure(background='black')
		self.display()

	def initIndexBar(self,lineNumber):
		indexStr = ""
		for i in range(1,lineNumber):
			if i == lineNumber - 1:
				indexStr = indexStr + str(i)
			else:
				indexStr = indexStr + str(i) + "\n"
		
		self.indexbar = Text(self.window, font=("Lucida Console", 12),height=42,width=3)
		self.indexbar.insert(INSERT, indexStr)
		self.indexbar.configure(state='disabled')
		self.indexbar.place(x=0,y=0)

	def WriteArea(self):
		# self.screenWidth = self.window.winfo_width()
		# self.screenHeight = self.window.winfo_height()

		maxRangeIndex = 43
		self.initIndexBar(maxRangeIndex)
		self.AreaCode = Text(self.window,height=42,width=200)
		self.AreaCode.place(x=40,y=0)


	def TerminalArea(self):
		self.terminal = Text(self.window,height=15,width=203,background='grey')
		self.terminal.insert(INSERT, "")
		self.terminal.configure(state='disabled')
		self.terminal.place(x=0,y=680)

	def MainMenu(self):
		self.menuBar = Menu(self.window)
		self.window.config(menu=self.menuBar)
		self.menufichier = Menu(self.menuBar,tearoff=0)
		self.menuBar.add_cascade(label="Fichier", menu=self.menufichier)
		self.menuBar.add_command(label="Executer",command=self.RunCode)
		self.menufichier.add_command(label="Ouvrir", command=self.OpenFile)
		self.menufichier.add_command(label="Enregistrer", command=self.SaveFile)
		self.menufichier.add_command(label="Enregistrer sous", command=self.SaveFile)
		self.menufichier.add_command(label="Quitter",command=self.window.quit) 

	def currentUser(self):
		return os.getlogin()

	def browseFiles(self):
		self.filename = filedialog.askopenfilename(initialdir = self.userPath, title = "Select a File", filetypes = (("Python files","*.py*"),("all files","*.*")))
		return self.filename

	# Run file Function
	def OpenFile(self):
		self.pathFile = self.fileName = self.browseFiles()
		f = open(self.fileName, "r")
		self.num_lines = sum(1 for line in open(self.pathFile))
		self.initIndexBar(self.num_lines)
		self.stringValue = f.read()
		self.stringValue = str(self.stringValue)
		self.AreaCode.delete('1.0', 'end')
		self.AreaCode.insert("1.0", self.stringValue)
		f.close()


	def RunCode(self):
		if self.pathFile == "":
			# not save
			self.SaveFile()
			if self.pathFile != "":
				self.Terminal('py ' + self.pathFile)
			else:
				print('error')
		else:
			self.Terminal('py ' + self.pathFile)
		self.updateTerm()

	def SaveFile(self):
		stringFile = self.AreaCode.get("1.0",'end')
		if self.pathFile == "":
			try:
				f = filedialog.asksaveasfile(mode='w', defaultextension=".py", initialdir = self.userPath)
				self.pathFile = f.name
				f.write(stringFile)
				f.close()
				print('save')
			except:
				print("File not opened")
		else:
			f = open(self.fileName, "w")
			f.write(stringFile)
			print('save')

	def getClass(self):
		return self.window

	def display(self):
		self.WriteArea()
		self.MainMenu()
		self.TerminalArea()
		self.window.mainloop()

	def updateTerm(self):
		self.output = self.replaceOutTerm(str(self.output))
		self.outError = self.replaceOutTerm(str(self.outError))

		command = ""
		for i in range(0,len(self.args)):
			command = command + self.args[i] + " "

		# outPut = self.output
		self.terminal.configure(state='normal')
		self.terminal.insert(INSERT,'\n' + self.userPath + '>' + command + '\n' + self.output.strip() + self.outError.strip() + '\n')
		self.terminal.configure(state='disabled')
		
	def replaceOutTerm(self,string):
		str = string.replace("b''", "")
		str = str.replace("b'", "")
		str = str.replace("'", "")
		str = str.replace("\\n", "\n")
		str = str.replace("\\r", "")
		return str

	def Terminal(self,command):
		command_summary = command.split(' ')
		os.environ["PYTHONUNBUFFERED"] = "1"
		result = subprocess.run(command_summary, shell = True, env = os.environ, capture_output=True)
		self.args = result.args
		self.outError = result.stderr
		self.output = result.stdout

H1 = IDE()
