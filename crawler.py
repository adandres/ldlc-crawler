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

Chipset = {
		"AMD 760G" : 1,
		"AMD A320" : 2,
		"AMD A520" : 3,
		"AMD B350" : 40,
		"AMD B450" : 4,
		"AMD B550" : 5,
		"AMD TRX40" : 6,
		"AMD WRX80" : 7,
		"AMD X370" : 8,
		"AMD X399" : 9,
		"AMD X470" : 10,
		"AMD X570" : 11,
		"Intel B360 Express" : 12,
		"Intel B365 Express" : 13,
		"Intel B460 Express" : 14,
		"Intel B560 Express" : 15,
		"Intel C224" : 16,
		"Intel C232" : 17,
		"Intel C246" : 18,
		"Intel C422" : 19,
		"Intel C612" : 20,
		"Intel C621" : 21,
		"Intel C622" : 22,
		"Intel H310 Express" : 23,
		"Intel H370 Express" : 24,
		"Intel H410 Express" : 25,
		"Intel H470 Express" : 26,
		"Intel H510 Express" : 27,
		"Intel H570 Express" : 28,
		"Intel Q470 Express" : 38,
		"Intel Q570 Express" : 29,
		"Intel SoC (System on Chip)" : 30,
		"Intel W480" : 31,
		"Intel X299 Express" : 32,
		"Intel Z370 Express" : 39,
		"Intel Z390 Express" : 33,
		"Intel Z490 Express" : 34,
		"Intel Z590 Express" : 35,
		"N/A" : 36,
		"SoC AMD FT3" : 37
	}

Socket = {
		"AMD AM3" : 1,
		"AMD AM3+" : 2,
		"AMD AM4" : 3,
		"AMD SP3" : 4,
		"AMD sTR4" : 5,
		"AMD sTRx4" : 6,
		"AMD sWRX8" : 7,
		"Intel 1150" : 8,
		"Intel 1151" : 9,
		"Intel 1200" : 10,
		"Intel 2011-v3" : 11,
		"Intel 2066" : 12,
		"Intel LGA3647" : 13,
		"N/A" : 14
	}

Frequence = {
		"DDR2 667 MHz" : 1,
		"DDR2 800 MHz" : 2,
		"DDR3 1066 MHz" : 3,
		"DDR3 1333 MHz" : 4,
		"DDR3 1600 MHz" : 5,
		"DDR3 1866 MHz" : 6,
		"DDR3 2133 MHz" : 7,
		"DDR3 2400 MHz" : 8,
		"DDR4 1866 MHz" : 9,
		"DDR4 2133 MHz" : 10,
		"DDR4 2400 MHz" : 11,
		"DDR4 2666 MHz" : 12,
		"DDR4 2800 MHz" : 13,
		"DDR4 2933 MHz" : 14,
		"DDR4 3000 MHz" : 15,
		"DDR4 3200 MHz" : 16,
		"DDR4 3300 MHz" : 17,
		"DDR4 3333 MHz" : 18,
		"DDR4 3400 MHz" : 19,
		"DDR4 3466 MHz" : 20,
		"DDR4 3600 MHz" : 21,
		"DDR4 3666 MHz" : 22,
		"DDR4 3733 MHz" : 23,
		"DDR4 3800 MHz" : 24,
		"DDR4 3866 MHz" : 25,
		"DDR4 4000 MHz" : 26,
		"DDR4 4133 MHz" : 27,
		"DDR4 4200 MHz" : 28,
		"DDR4 4266 MHz" : 29,
		"DDR4 4300 MHz" : 30,
		"DDR4 4333 MHz" : 31,
		"DDR4 4400 MHz" : 32,
		"DDR4 4500 MHz" : 33,
		"DDR4 4600 MHz" : 34,
		"DDR4 4700 MHz" : 35,
		"DDR4 4800 MHz" : 36,
		"DDR4 5000 MHz" : 37,
		"DDR4 5066 MHz" : 38,
		"DDR4 5133 MHz" : 39,
		"DDR4 5333 MHz" : 40

	}

toDitch = {
		'Utilisation type',
		'Gamer',
		'Version Boîte',
		'Ces timings sont supportés avec une tension minimale de :',
		'Garantie légale',
		'Optimisé Apple',
		'Roulement à billes',
		'Top Flow',
		'Double tour',
		'Matériau(x)',
		'Niveau sonore mini',
		'Débit d\'air mini',
		'Support TPM (Trusted Platform Module)',
		'Norme de Sortie DVI',
		'Compatibilité PSU-CM',
		'Norme alimentation',
		'Contrôleur'
	}

toFloat = {
		'Fréquence CPU',
		'Fréquence en mode Turbo',
		'Hauteur (ventilateur inclus)',
		'Largeur (ventilateur inclus)',
		'Profondeur (ventilateur inclus)',
		'Poids',
		'Hauteur',
		'Longueur',
		'Largeur',
		'Profondeur',
		'Epaisseur'
	}

toInt = {
		'Nombre de core',
		'Nombre de Threads',
		'Capacité',
		'Nombre de barrettes',
		'Capacité par barrette',
		'CAS Latency',
		'RAS to CAS Delay',
		'RAS Precharge Time',
		'RAS Active Time',
		'TDP Max. CPU',
		'Diamètre ventilateur',
		'Vitesse de rotation mini',
		'Vitesse de rotation maxi',
		'Nombre de CPU supportés',
		'Nombre de canaux audio',
		'Nombre de connecteurs pour ventilateurs',
		'Nombre de GPU',
		'Taille mémoire vidéo',
		'Nombre d\'écran(s)',
		'Consommation',
		'Taille de ventilateur',
		'Puissance',
		'Taille du cache',
		'Vitesse en lecture',
		'Vitesse en écriture',
		'IOPS'
	}

DBTable = [
		"Processeur",
		"RAM",
		"Refroidissement",
		"Mobo",
		"GPU",
		"Alimentation",
		"SSD",
	]


link = [
		"https://www.ldlc.com/informatique/pieces-informatique/processeur/c4300/",
		"https://www.ldlc.com/informatique/pieces-informatique/memoire-pc/c4703/",
		"https://www.ldlc.com/informatique/pieces-informatique/radiateur-processeur/c4712/",
		"https://www.ldlc.com/informatique/pieces-informatique/carte-mere/c4293/",
		"https://www.ldlc.com/informatique/pieces-informatique/carte-graphique-interne/c4684/",
		"https://www.ldlc.com/informatique/pieces-informatique/alimentation-pc/c4289/",
		"https://www.ldlc.com/informatique/pieces-informatique/disque-ssd/c4698/",
	]



def IsJSON(index, lname):
	if lname in {'Compatibilité chipset carte mère', 'Virtualisation', 'Fréquence(s) Mémoire'} and index == 0:
		return True
	if lname in {'Support du processeur', 'Connecteur(s)'} and index == 2:
		return True
	if lname in {'Support du processeur', 'Fréquence(s) Mémoire', 'Connecteur(s) graphique', 'Connecteurs Disques', 'Modes RAID supportés', 'Connecteurs panneau arrière', 'Connecteurs additionnels', 'Ports USB'} and index == 3:
		return True
	if lname in {'Sorties vidéo'} and index == 4:
		return True
	if lname in {'Multi-GPU', 'Connecteur(s) alimentation'} and index == 5:
		return True
	return False
	

def saveInDB(cursor, index, indexArray, valArray):

	strval = '%s' + ', %s' * (len(valArray) - 1)
	table = DBTable[index]
	sql = 'INSERT INTO ' + table + ' (`' + '`, `'.join(indexArray) + '`) VALUES (' + strval + ')'
	try:
		cursor.execute(sql, valArray)
	except mysql.connector.Error as err:
  		print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nSomething went wrong: {}\n\n".format(err))


def crawler(cursor, index, pageMax = 3):
	npage = 1
	while npage < pageMax:
		print("page: " + str(npage))
		URL = link[index]
		if (npage > 1):
			URL = link[index] + 'page' + str(npage)
		print(URL)
		page = requests.get(URL, headers)
		soup = BeautifulSoup(page.content, 'html.parser')
		items = soup.findAll('li', ['pdt-item'])
		if items is None:
			exit()
		for item in items:
			print(item.find('div', ['basket']))
			#print(item.a['href'])
			spider(cursor, index, item.a['href'])
		npage += 1

def spider(cursor, index, URL):
	URL = "https://www.ldlc.com" + URL
	print(URL)
	page = requests.get(URL, headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	items = soup.find('div', ['specsTech'])
	photo = soup.find('div', id='productphoto')
	photo = photo.find('img')
	print(photo['src'])
	desc = soup.find('p', ['desc'])
	print(desc)
	prix = soup.find('div', ['price'])
	print(prix)
	items = items.findAll('tr')
	data, indexArray, valArray = [], [], []
	c, cn, ut = 0, 0, 0
	val, name, lname = None, None, None
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
			if name is None or name.text not in toDitch:
				link = cols.text
				val = " ".join(link.split())
				if name is not None:
					name = name.text
					if (name == 'Utilisation'):
						ut += 1
						if ut == 2 or index == 3 or index == 4:
							ut = cn	
					if name in toFloat:
						val = float(val.split()[0])
					elif name in toInt:
						val = int(val.split()[0])
					indexArray.append(name)
					if IsJSON(index, lname):
						valArray.append(data)
					elif c > 0:
						valArray.append(data[0])
					if data is not None and c > 0:
						data = []
					lname = name
					cn += 1
				if val in Socket.keys():
					val = Socket[val]
				elif val in Chipset.keys():
					val = Chipset[val]
				elif val in Frequence.keys():
					val = Frequence[val]
				data.append(val)
		c += 1
	if len(data) == 1 and c > 0:
		valArray.append(data[0])
	elif c > 0:
		valArray.append(data)
	if ut > 2:
		indexArray.pop(ut)
		valArray.pop(ut)
	print("ok")
	saveInDB(cursor, index, indexArray, valArray)


connection = mysql.connector.connect(
					host='localhost',
					unix_socket='/Applications/MAMP/tmp/mysql/mysql.sock',
					database='Ecommerce',
                                       	user='root',
                                       	password='root'
				)
cursor = connection.cursor()
index = 6
while index < len(link):
	crawler(cursor, index)
	connection.commit()
	index += 1
cursor.close()
connection.close()
