'''
Dit programma is gemaakt voor het Technasium van het Calandlyceum.

Gemaakt door Auke Schuringa.
'''

import sys
import re
import time

def convert_month(premonth):
	if re.match(r'[0-9]', premonth):
		months = ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]
		if len(str(premonth)) > 2 or int(premonth) > 12:
			raise ValueError('De maand is maximaal twee cijfer lang. Bijvoorbeeld: mei of 5 of 05')
		else:
			return str(months[int(premonth)-1])
	else:
		return premonth

def date(sort):
	year = raw_input("--> Jaar van {0}: ".format(sort))
	while year == "info" or year == "Info":
		print("Geef hier het jaar van {0} van de bron op die je wilt gebruiken. Bijvoorbeeld:".format(sort))
		print(" - 2011")
		print("(Zonder ' - '.)")
		year = raw_input("--> Jaar van {0}: ".format(sort))
	if year:
		month = raw_input("--> Maand van {0}: ".format(sort))
		while month == "info" or month == "Info":
			print("Geef hier de maand van {0} van de bron op die je wilt gebruiken. Bijvoorbeeld:".format(sort))
			print(" - mei")
			print(" - 5")
			print(" - 05")
			print("(Zonder ' - '.)")
			month = raw_input("--> Maand van {0}: ".format(sort))
		if month:
			day = raw_input("--> Dag van {0}: ".format(sort))
			while day == "info" or day == "Info":
				print("Geef hier de dag van {0} van de bron op die je wilt gebruiken. Bijvoorbeeld:".format(sort))
				print(" - 5")
				print(" - 05")
				print(" - 23")
				print("(Zonder ' - '.)")
				day = raw_input("--> Dag van {0}: ".format(sort))
			if day:
				if sort == "publicatie":
					return "{0}, {1} {2}".format(str(int(year)), str(int(day)), convert_month(month))
				elif sort == "het bekijken":
					return "{0} {1}, {2},".format(str(int(day)), convert_month(month), str(int(year)))
			else:
				print("Dag van {0} is onbekend.".format(sort))
				if sort == "publicatie":
					return "{0}, {1}".format(str(int(year)), convert_month(month))
				elif sort == "het bekijken":
					return "{0}, {1},".format(convert_month(month), str(int(year)))
		else:
			print("Maand van {0} is onbekend, een dag van {0} is dus ook niet nodig.".format(sort))
			return str(int(year))
	else:
		print("Jaar van {0} in onbekend, een maand en een dag van {0} zijn dus ook niet nodig.".format(sort))
		if sort == "publicatie":
			return "z.d."
		elif sort == "het bekijken":
			print("De datum van vandaag wordt gebruikt als tijd van {0}.".format(sort))
			return "{0} {1}, {2},".format(str(int(time.strftime("%d"))), convert_month(time.strftime("%m")), time.strftime("%Y"))

def internetartikel():
	print("Druk op [enter] zonder invoer als iets niet bekend is.")
	print("Type 'info' als je meer informatie nodig hebt voor het opgeven van tekst.")
	title = raw_input("--> Titel van publicatie: ")
	while title == "info" or title == "Info" or not title:
		print("Geef hier de titel van de bron op die je wilt gebruiken. Een titel is verplicht. Bijvoobeeld:")
		print(" - Media Spun Up on NASA Cutting-edge Mars Landing Technology")
		print(" - Wind speelt Schiphol weer parten")
		print(" - 'Zoeken op internet laat mensen denken dat ze slim zijn'")
		print(" - Volunteer with Mozilla!")
		print("(Zonder ' - '.)")
		title = raw_input("--> Titel van publicatie: ")
	author = raw_input("--> Auteur van publicatie: ")
	while author == "info" or author == "Info":
		print("Geef hier de auteur (de schrijver) van de bron op die je wilt gebruiken. Bijvoorbeeld:")
		print(" - Auke Schuringa")
		print(" - Krijn Soeteman")
		print(" - Wim van Heusden")
		print(" - Juliana Louise Emma Marie Wilhelmina van Oranje-Nassau")
		print("(Zonder ' - '.)")
		author = raw_input("--> Auteur van publicatie: ")
	if not author:
		print("Auteur van publicatie is onbekend.")
		author = raw_input("--> Verspreider van publicatie: ")
		while author == "info" or author == "Info" or not author:
			print("Geef hier de verspreider van de bron op die je wilt gebruiken. Deze stap is verplicht als de auteur niets bekend is. Bijvoorbeeld:")
			print(" - tweakers")
			print(" - NOS")
			print(" - nu.nl")
			print("(Zonder ' - '.)")
			author = raw_input("--> Verspreider van publicatie: ")
	pubdate = date("publicatie")
	viewdate = date("het bekijken")
	url = raw_input("--> Url van publicatie: ")
	while url == "info" or url == "Info" or not url or not ("http://" in url or "https://" in url):
		print("Geef hier de titel van de bron op die je wilt gebruiken. Een url (link) naar de bron met 'http://' of 'https://' is verplicht. Bijvoobeeld:")
		print(" - http://nos.nl/artikel/2028024-wind-speelt-schiphol-weer-parten.html")
		print(" - http://tweakers.net/nieuws/102234/eerste-sites-op-amsterdam-domein-gaan-live.html")
		print("(Zonder ' - '.)")
		url = raw_input("--> Url van publicatie: ")
	print("Bij deze bron kun je de volgende bronvermelding gebruiken:")
	print("{0}. ({1}). {2}. Geraadpleegd op {3} van {4}.".format(author, pubdate, title, viewdate, url))

def main():
	referenties = ["Artikel op het internet"]
	print("Type het nummer van de soort bron waar je naar wilt refereren.")
	for referentie in referenties:
		print("{0} = {1}".format(str(referenties.index('{0}'.format(referentie))+1), referentie))
	referentie = raw_input("Nummer van de bron: ")
	if int(referentie) == 1:
		internetartikel()


if __name__ == '__main__':
	main()
