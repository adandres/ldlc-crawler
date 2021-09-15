import requests
from bs4 import BeautifulSoup
import mysql.connector
from mysql.connector import Error
import json


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

toDitch = {'Utilisation type', 'Gamer', 'Version Boîte', 'Ces timings sont supportés avec une tension minimale de :', 'Garantie légale', 'Optimisé Apple', 'Roulement à billes', 'Top Flow', 'Double tour', 'Matériau(x)', 'Niveau sonore mini', 'Débit d\'air mini'}

toFloat = { 'Fréquence CPU', 'Fréquence en mode Turbo', 'Hauteur (ventilateur inclus)', 'Largeur (ventilateur inclus)', 'Profondeur (ventilateur inclus)', 'Poids' }

toInt = {'Nombre de core', 'Nombre de Threads', 'Capacité', 'Nombre de barrettes', 'Capacité par barrette', 'CAS Latency', 'RAS to CAS Delay', 'RAS Precharge Time', 'RAS Active Time', 'TDP Max. CPU', 'Diamètre ventilateur', 'Vitesse de rotation mini', 'Vitesse de rotation maxi'}

DBTable = {"Processeur", "`RAM`", "Refroidissement", "Motherboard"}
Link = {"https://www.ldlc.com/informatique/pieces-informatique/processeur/c4300", "https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/", "https://www.ldlc.com/informatique/pieces-informatique/radiateur-processeur/c4712/"}
######################################################### CPU	

def saveProcInDB(index, val):
	connection = mysql.connector.connect(host='localhost',unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
					database='Ecommerce',
                                         user='root',
                                         password='root')
	cursor = connection.cursor()
	strval = '%s' + ', %s' * (len(valArray) - 1)
	sql = 'INSERT INTO Processeur (`' + '`, `'.join(indexArray) + '`) VALUES (' + strval + ')'
	try:
		cursor.execute(sql, valArray)
	except mysql.connector.Error as err:
  		print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSomething went wrong: {}\n\n".format(err))
	connection.commit()
	cursor.close()
	connection.close()



def crawler_proc():
	npage = 1
	while 1:
		print("page: " + str(npage))
		if (npage == 1):
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/processeur/c4300'
		else:
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/processeur/c4300/page' + str(npage)
		print(URL)
		page = requests.get(URL, headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		items = soup.findAll('li', ['pdt-item'])
		if items is None:
			exit()
		for item in items:
			print(item.a['href'])
			#spider_proc(item.a['href'])
		npage += 1
		if npage == 4:
		 exit()




def spider_proc(URL):
	URL = "https://www.ldlc.com" + URL
	page = requests.get(URL, headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	items = soup.find('div', ['specsTech'])
	items = items.findAll('tr')
	data = []
	indexArray = []
	valArray = []
	c = 0
	val = None
	name = None
	lname = None
	l = len(items)
	for item in items:
		print(item)
		print(c)
		if c == 0 or c == 2:
			cols = item.find('td', ['checkbox'])
			print(cols)
		elif c == l - 2:
			cols = item.find('td', ['no-checkbox'])
		else:
			cols = item.find('a')
		if cols is not None and c < l - 1:
			name = item.h3
			if name is None or name.text not in {'Utilisation type', 'Gamer', 'Version Boîte', 'Garantie légale'}:
				link = cols.text
				val = " ".join(link.split())
				if name is not None:
					name = name.text	
					if name in {'Fréquence CPU', 'Fréquence en mode Turbo'}:
						val = float(val.split()[0])
					elif name in {'Nombre de core', 'Nombre de Threads'}:
						val = int(val.split()[0])
					indexArray.append(name)
					if lname in {'Compatibilité chipset carte mère', 'Virtualisation', 'Fréquence(s) Mémoire'}:
						valArray.append(json.dumps(data))
					elif c > 0:
						valArray.append(data[0])
					if data is not None and c > 0:
						data = []
				data.append(val)
		c += 1
	if len(data) == 1 and c > 0:
		valArray.append(data[0])
	elif c > 0:
		valArray.append(data)
	#print(index#Array)
	#print(valArray)
	#print(len(indexArray))
	#print(len(valArray))
	saveInDB(indexArray, valArray)


#spider('https://www.ldlc.com/fiche/PB00256786.html')
#crawler_proc()

######################################################################### RAM

def saveRAMInDB(indexArray, valArray):
	connection = mysql.connector.connect(host='localhost',unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
					database='Ecommerce',
                                         user='root',
                                         password='root')
	cursor = connection.cursor()
	strval = '%s' + ', %s' * (len(valArray) - 1)
	sql = 'INSERT INTO RAM (`' + '`, `'.join(indexArray) + '`) VALUES (' + strval + ')'
	try:
		cursor.execute(sql, valArray)
	except mysql.connector.Error as err:
  		print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSomething went wrong: {}\n\n".format(err))
	connection.commit()
	cursor.close()
	connection.close()



def crawler_RAM():
	npage = 1
	while 1:
		print("page: " + str(npage))
		if (npage == 1):
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/'
		else:
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/page' + str(npage)
		print(URL)
		page = requests.get(URL, headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		items = soup.findAll('li', ['pdt-item'])
		if items is None:
			exit()
		for item in items:
			#print(item.a['href'])
			spider_RAM(item.a['href'])
		npage += 1
		if npage == 34:
		 exit()




def spider_RAM(URL):
	URL = "https://www.ldlc.com" + URL
	print(URL)
	page = requests.get(URL, headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	items = soup.find('div', ['specsTech'])
	items = items.findAll('tr')
	data = []
	indexArray = []
	valArray = []
	c = 0
	val = None
	name = None
	lname = None
	l = len(items)
	for item in items:
		if c == 0 or c == 2:
			cols = item.find('td', ['checkbox'])
		elif c == l - 2:
			cols = item.find('td', ['no-checkbox'])
		else:
			cols = item.find('a')
		if cols is not None and c < l - 1:
			name = item.h3
			if name is None or name.text not in {'Utilisation type', 'Ces timings sont supportés avec une tension minimale de :', 'Garantie légale', 'Optimisé Apple'}:
				link = cols.text
				val = " ".join(link.split())
				if name is not None:
					name = name.text
					if name in {'Capacité', 'Nombre de barrettes', 'Capacité par barrette', 'CAS Latency',
							'RAS to CAS Delay', 'RAS Precharge Time', 'RAS Active Time'}:
						val = int(val.split()[0])
					indexArray.append(name)
					if c > 0:
						valArray.append(data[0])
					if data is not None and c > 0:
						data = []
					lname = name
				data.append(val)
		c += 1
	if len(data) == 1 and c > 0:
		valArray.append(data[0])
	elif c > 0:
		valArray.append(data)
	#print(indexArray)
	#print(valArray)
	#print(len(indexArray))
	#print(len(valArray))
	saveRAMInDB(indexArray, valArray)

#crawler_RAM()

########################################################### refroidissement

def saveVentInDB(indexArray, valArray):
	connection = mysql.connector.connect(host='localhost',unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
					database='Ecommerce',
                                         user='root',
                                         password='root')
	cursor = connection.cursor()
	strval = '%s' + ', %s' * (len(valArray) - 1)
	sql = 'INSERT INTO `Refroidissement` (`' + '`, `'.join(indexArray) + '`) VALUES (' + strval + ')'
	try:
		cursor.execute(sql, valArray)
	except mysql.connector.Error as err:
  		print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSomething went wrong: {}\n\n".format(err))
	connection.commit()
	cursor.close()
	connection.close()



def crawler_Vent():
	npage = 1
	while 1:
		print("page: " + str(npage))
		if (npage == 1):
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/radiateur-processeur/c4712/'
		else:
			URL = 'https://www.ldlc.com/informatique/pieces-informatique/radiateur-processeur/c4712/page' + str(npage)
		print(URL)
		page = requests.get(URL, headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		items = soup.findAll('li', ['pdt-item'])
		if items is None:
			exit()
		for item in items:
			#print(item.a['href'])
			spider_Vent(item.a['href'])
		npage += 1
		if npage == 34:
		 exit()




def spider_Vent(URL):
	URL = "https://www.ldlc.com" + URL
	print(URL)
	page = requests.get(URL, headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	items = soup.find('div', ['specsTech'])
	items = items.findAll('tr')
	data = []
	indexArray = []
	valArray = []
	c = 0
	cn = 0
	ut = 0
	val = None
	name = None
	lname = None
	l = len(items)
	for item in items:
		if c == 0 or c == 2:
			cols = item.find('td', ['checkbox'])
		elif c == l - 2:
			cols = item.find('td', ['no-checkbox'])
		else:
			cols = item.find('a')
		if cols is not None and c < l - 1:
			name = item.h3
			if name is None or name.text not in {'Roulement à billes', 'Top Flow', 'Double tour', 'Matériau(x)', 'Niveau sonore mini', 'Débit d\'air mini'}:
				link = cols.text
				val = " ".join(link.split())
				if name is not None:
					name = name.text
					if (name == 'Utilisation'):
						ut += 1
						if ut == 2:
							ut = cn	
					if name in {'Hauteur (ventilateur inclus)', 'Largeur (ventilateur inclus)', 'Profondeur (ventilateur inclus)', 'Poids'}:
						val = float(val.split()[0])
					elif name in {'TDP Max. CPU', 'Diamètre ventilateur', 'Vitesse de rotation mini', 'Vitesse de rotation maxi'}:
						val = int(val.split()[0])
					indexArray.append(name)
					if lname in {'Support du processeur', 'Connecteur(s)'}:
						valArray.append(json.dumps(data))
					elif c > 0:
						valArray.append(data[0])
					if data is not None and c > 0:
						data = []
					lname = name
					cn += 1
				data.append(val)
		c += 1
	if len(data) == 1 and c > 0:
		valArray.append(data[0])
	elif c > 0:
		valArray.append(data)
	indexArray.pop(ut)
	valArray.pop(ut)
	print(indexArray)
	print(valArray)
	print(len(indexArray))
	print(len(valArray))
	saveVentInDB(indexArray, valArray)

crawler_Vent()

