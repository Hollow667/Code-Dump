import time

print('\n' * 100)
print('\n\n[-Aventurile lui Dognald Trump (DEMO): by Zero Davila -]')
print('''\n
===========================================================================================
                                        DOGELAND 2016
===========================================================================================''')
print('\nLoading : DogeLand.')
time.sleep(.5)
print('\nLoading : Ovar office')
time.sleep(.5)
print('\nLoading : Death Star')
time.sleep(.5)
print('\nLoading : Dognald Trump')
time.sleep(.5)
print('\nLoading : Hittlary Clinton')
time.sleep(.5)
print('\nLoading : Birdy Sanchez')
time.sleep(.5)
print('\nLoading : Vagdimir Pugtin')
time.sleep(.5)
print('\nLoading : Sahara Palin')
time.sleep(.5)
print('\nLoading : Obagnana')
time.sleep(.5)
print('\nLoading : StormTroopers')
time.sleep(.5)
print('\nAll microcephaly components loaded.')
time.sleep(1)

print('''\n\n
	===============================================================================================
	- Domnul Dognald Trump, bine a-ti ajuns in parcarea imperiului DogeLand.
	Obiectivul e sa va prezentati la conducerea biroului ovar evitand pericole si calcand
	peste sufletele nesemnificative ale inamicilor. In zile ca astea nu putem avea
	incredere in nimeni, nici macar in noi. Colectati un imprumut mic de un milion de
	dolari, luati un zid de caramida in caz de mexicani, aranjati peruca si avansati catre intrare.
	===============================================================================================''')

def start(inventory):
	print('\n==== Hol ====')
	time.sleep(1)
	print('...')
	time.sleep(1)
	print('\n[-HOL PRINCIPAL-]')
	print('\n1.) opt 1 - Prima usa')
	print('\n2.) opt 2 - A doua usa')
	print('\n3.) opt 3 - A treia usa')
	print('\n4.) opt 4 - Verifica inventarul')
	print('\n4.) opt 5 - Iesire')

	cmdlist = ['1', '2', '3', '4', '5']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		usa1(inventory)
	elif cmd == '2':
		usa2(inventory)
	elif cmd == '3':
		usa3(inventory)
	elif cmd == '4':
		inventar(inventory)
	elif cmd == '5':
		exit(inventory)

def exit(inventory):
	print('...')
	time.sleep(1)
	print('Bye')
	time.sleep(1)
	print('\n...')
	time.sleep(1)
	quit

def inventar(inventory):
	print('\n	Inventar :')
	time.sleep(.5)
	print('\n	===========================================')
	time.sleep(.5)
	print('\n	[+] un zid de caramida')
	time.sleep(.5)
	print('	[+] o poza cu degetele proprii')
	time.sleep(.5)
	print('	[+] a pyro that must learn how to spoken')
	time.sleep(.5)
	print('	[+] o peruca')
	time.sleep(.5)
	print('	[+] un imprumut mic de un milion de dolari')
	time.sleep(.5)
	print('\n	===========================================')
	time.sleep(.5)
	start(inventory)

def usa1(inventory):
	print('\n==== Incapere 1 ====')
	time.sleep(1)
	print('...')
	time.sleep(1)
	print('''\n
	==================================================================================================
	- Intri intr-o camera intunecata cu un glob de cristal in centru, e luminat de sperantele si
	visele clasei mijlocii, iti poti da seama pentru ca numarul de lumeni scade exponential de cand
	ai intrat in incapere. Din umbra apar 3 fiinte preistorice imbracate in tinuta clasica gregoriana,
	Birdy Sanchez care fluiera ca e anti-sistem chiar daca sa alaturat sistemului imediat dupa
	primul esec, messia Obagnana care te vorbeste de rau, iar Sahara Palin e doar acolo
	pentru a admira teritoriul rusiei.
	==================================================================================================''')
	print('[-INCAPERE 1-]\n')
	print('1.) Priveste globul')
	print('2.) Vorbeste')
	print('3.) Paraseste camera')

	cmdlist =['1', '2', '3']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		print('\n...')
		time.sleep(1)
		print('\n[-PRIVIND GLOBUL-]')
		print('''\n
	===================================================================================================
	- Te apropii usor de cristal, cu fiecare pas vezi o lume in care oamenii stiu cum functioneaza
	bancile centrale, costumele care scriu legislatia inteleg cum functioneaza DNS, lumea inceteaza
	din a consuma BiBC, Mikey Nimaj, si CardAshian, si poate, realizeaza esenta naturii umane.
	Poate isi vor pune intrebari si vor realiza ca nu au nevoie de conducere pentru a fi civilizati,
	pentru a fi o societate si a coloniza stelele impreuna, poate tot ce au cunoscut de mii de
	ani ca fiind norma a fost o scamatorie de proportii astronomice. Contemplezi impactul denigrant
	care l-ar avea asupra campaniei tale politice si iti vine sa vomiti, colorezi papucii lui Obagnana
	si iesi urgent pe usa.
	===================================================================================================''')
		time.sleep(2)
		start(inventory)
	elif cmd == '2':
		print('\n...')
		time.sleep(1)
		print('\n[-COMUNICARE-]')
		print('''\n
	=============================================================================================
	- Ai atentat o comunicare amicala dar din nefericire, au folosit mai mult decat cuvinte
	monosilabice, ai inceput sa sangerezi din orificii multiple si te cuprinde un atac de panica,
	simti ca ar fi o idee inteleapta sa te retragi din incapere.
	=============================================================================================''')
		print('1.)Paraseste camera')
		print('2.)Ramai')

		cmdlist = ['1','2']
		cmd = getcmd(cmdlist)

		if cmd == '1':
			start(inventory)

		elif cmd == '2':
			print('...')
			time.sleep(1)
			print('Deces gramatic')
			time.sleep(1)
			print('...')
			print('Bye')
			time.sleep(1)
			quit

	elif cmd == '3':
		start(inventory)


def usa2(inventory):
	print('\n==== Incapere 2 ====')
	time.sleep(1)
	print('...')
	time.sleep(1)
	print('''\n
	==============================================================================================
	- Intri pe usa si primul lucru care il vezi e un Vagdimir Pugtin face public cine finanteaza cu
	adevarat organizatia PISIS cu obiecte falice. Obagnana transpira, dar pentru tine poate fi o
	oportunitate. Vocabularul nu iti permite sa participi intr-o conversatie unde nu poti folosi
	cuvintele mexicani, china si zid, dar din putina rusa care o intelegi ai impresia ca Pugtin
	te-a mentionat ca fiind drept geniu, tu dai usor din cap aproband.
	==============================================================================================''')
	print('[-INCAPERE 2-]\n')
	print('1.) Stanga')
	print('2.) Dreapta')

	cmdlist = ['1', '2']
	cmd = getcmd(cmdlist)

	if cmd == '1':
		print('\n...')
		time.sleep(1)
		print('''\n
	============================================================================================
	- Tragi cu urechea catre o conversatie in stanga si ai auzit de Brexit, ai realizat ca Scotia 
	este cu adevarat un exemplu demn de urmat, si-au lua tara inapoi, asa ca te gandesti sa 
	postezi asta pe twitter, in final, cu brexit, fara brexit, prabusirea economiei tot acelasi 
	gust are.
	============================================================================================''')
		usa2(inventory)

	elif cmd == '2':
		print('\n...')
		time.sleep(1)
		print('''\n
	==============================================================================================
	- Te-ai intors, ai facut 2 pasi, si neasteptat intalnesti viitoarea rezidenta a penitenciarului
	Hittlary Clinton, vorbind despre aceleasi aberatii retrograde fiindca poporul nu cunoaste
	istorie. Te cuprinde o anxietate si simti ca instinctele tale se vor manifesta curand.
	==============================================================================================''')
		print('\n1.) Zid')
		print('\n2.) Pyrocinical')
		print('\n3.) Poza')

		cmdlist = ['1', '2', '3']
		cmd = getcmd(cmdlist)

		if cmd == '1':
			print('''\n
	=================================================================================================
	- Fara sa te gandesti la faptul ca ar mai putea exista alte nevoi scoti un zid de caramida din 
	buzunar, il pui intre voi si fugi in directia opusa. Ai iesit din camera.
	=================================================================================================''')
			start(inventory)

		elif cmd == '2':
			print('''\n
	============================================================================================
	- Din senin scoti un pyro salbatic si il arunci in ea, she has forgotten how to spoken*. Fara
	abilitati de comunicare cu siguranta va pierde alegerile. Ai iesit din camera.
	============================================================================================''')
			start(inventory)

		elif cmd == '3':
			print('''\n
	===================================================================================================
	- Scoti o poza cu degetele tale din buzunar si o arati la toata incaperea pentru a-ti cimenta
	dominanta. Acum ca toata lumea isi stie locul esti liber sa parasesti camera, dar lasi poza in urma.
	===================================================================================================''')

def usa3(inventory):
	print('\n==== Incapere 3 ====')
	time.sleep(1)
	print('...')
	time.sleep(1)
	print('''\n
	===========================================================================================
	- Ai ajuns in biroul ovar in ciuda protestelor, propagandei, democratiei, constitutiei si al 
	instinctului de auto-conservare a rasei umane. De aici oamenii au nevoie de telefonul rosu sa 
	te contacteze. Dar nu suntem in anii '90, nimeni nu mai are telefon fix rosu, nu cred ca se 
	mai fabrica, asta nu e un film. Datorita singuratatii ai ajuns dement si alb dar nimeni
	nu a observat diferenta, ai inceput sa crezi ca esti la conducerea unui corp ceresc si ai
	umplut strazile de storm trooperi.
	===========================================================================================
	                              CONGRATULATIONS, GOD MOD ENGAGED
	===========================================================================================''')


def getcmd(cmdlist):
	cmd = input('\nINPT:> ')
	if cmd in cmdlist:
		return cmd
	else:
		print('\n   error. invalid command-\n')
		return getcmd(cmdlist)

if __name__ == "__main__":
	inventory = ['service port']
	start(inventory)
