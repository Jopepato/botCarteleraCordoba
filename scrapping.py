#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import the library used to query a website
import urllib2
import re
#import the Beautiful soup functions to parse the data returned from the website
from bs4 import BeautifulSoup

import logging
import telebot
from time import sleep

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOKEN = '330883133:AAHvkTpcFu8Z-0XR8JmfUsppRqL6BWTBSII' # Nuestro tokken del bot (el que @BotFather nos dió).
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

class Cine:
	def __init__(self):
		return None

	nombreCine_ = ''
	nombrePeliculas_ = []
	horarioPeliculas_ = []

	def getNombreCine(self):
		return self.nombreCine_

	def setNombreCine(self, nombreCine):
		self.nombreCine_ = nombreCine

	def getNombrePeliculas(self):
		return self.nombrePeliculas_

	def setNombrePeliculas(self, nombrePeliculas):
		self.nombrePeliculas_ = nombrePeliculas

	def getHorarioPeliculas(self):
		return self.horarioPeliculas_

	def setHorarioPeliculas(self, horarioPeliculas):
		self.horarioPeliculas_ = horarioPeliculas

	def printTotal(self):
		print self.getNombreCine()
		print self.getNombrePeliculas()
		print self.getHorarioPeliculas()
		return True

def encuentraDatosCine(stop):
	cartelera = 'http://www.carteleracordoba.com/'

	#Query the website and return the html to the variable 'page'
	page = urllib2.urlopen(cartelera)

	soup = BeautifulSoup(page, 'html.parser')

	aux = Cine()
	k = 0
	for i in soup.find_all(id='bloqueportadaa'):
		aux.nombreCine_ = str(i.h1.string)
		listaPeliculasAux = []
		listaHorariosAux = []
		for j in i.find_all('div', class_='pildora'):
			if j.a is not None:
				nombrePelicula = j.a.string	
				listaPeliculasAux.append(nombrePelicula)
				#print listaPeliculasAux
				p = re.compile('\d+:\d+')
				auxStringHorario = ''

				for horario in p.findall(str(j.h5)):
					auxStringHorario = auxStringHorario + horario + ' '

				listaHorariosAux.append(auxStringHorario)

		aux.nombrePeliculas_ = listaPeliculasAux
		aux.horarioPeliculas_ = listaHorariosAux
		if k == stop:
			break
		else:
			k = k+1

	return aux	

#TODO: Hacer función para los cines de verano

def cinesDeVerano():
	#Esto va a devolver la cadena ya directa con los cines de verano
	cartelera = 'http://www.carteleracordoba.com/'

	#Query the website and return the html to the variable 'page'
	page = urllib2.urlopen(cartelera)

	soup = BeautifulSoup(page)
	cadenaCinesDeVerano = ''
	aux = Cine()
	k = 0
	for i in soup.find_all(id='bloqueportadaa'):
		aux.nombreCine_ = str(i.h1.string)
		listaPeliculasAux = []
		listaHorariosAux = []
		for j in i.find_all('div', class_='pildora'):
			nombrePelicula = j.a.string	
			listaPeliculasAux.append(nombrePelicula)
			#print listaPeliculasAux
			p = re.compile('\d+:\d+')
			auxStringHorario = ''

			for horario in p.findall(str(j.h5)):
				auxStringHorario = auxStringHorario + horario + ' '

			listaHorariosAux.append(auxStringHorario)

		aux.nombrePeliculas_ = listaPeliculasAux
		aux.horarioPeliculas_ = listaHorariosAux
		if (k == 0 or k == 1 or k == 4 or k == 5 or k == 6):
			cadenaCinesDeVerano = cadenaCinesDeVerano + "<b>" + aux.nombreCine_ + "</b>" + '\n'
			p = 0
			for q in aux.nombrePeliculas_:
				cadenaCinesDeVerano = cadenaCinesDeVerano + q + '\n'
				cadenaCinesDeVerano = cadenaCinesDeVerano + "<i>" + aux.horarioPeliculas_[p] + "</i>" + '\n'
				p = p+1
			cadenaCinesDeVerano = cadenaCinesDeVerano + '\n'
		k = k+1

	return cadenaCinesDeVerano

def daFormatoCadena(horariosCine):
	#Con esta funcion nos viene un objeto de la clase cine e intentamos montar una cadena que no quede mal
	cadena = ""
	j=0
	for i in horariosCine.nombrePeliculas_:
		#Vamos metiendo un salto de linea por pelicula y horario
		cadena = cadena + "<b>" + i + "</b>" +  '\n'
		cadena = cadena + "<i>" + horariosCine.horarioPeliculas_[j] +"</i>" + '\n\n'
		j = j+1
	return cadena

#Funciones

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hey, ve pillando palomitas que nos vamos al cine.")
	print "[" + str(message.chat.id) + "]: " + message.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 

@bot.message_handler(commands=['tablero']) # Indicamos que lo siguiente va a controlar el comando '/roto2'.
def command_cineTablero(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    #Tenemos que coger el cine y devolveremos los horarios que queremos
    horarios = encuentraDatosCine(7)
    #horarios.printTotal()
    mensajeDevuelta= daFormatoCadena(horarios)
    bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')
    #Vamos a intentar parsear un poco el mensaje


@bot.message_handler(commands=['guadalquivir']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_cineGuadalquivir(m): # Definimos una función que resuleva lo que necesitemos.
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	horarios = encuentraDatosCine(2)
	mensajeDevuelta= daFormatoCadena(horarios)
	bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')

@bot.message_handler(commands=['lucena'])
def command_cineLucena(m):
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	horarios = encuentraDatosCine(3)
	mensajeDevuelta= daFormatoCadena(horarios)
	bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')

@bot.message_handler(commands=['cinesDeVerano'])
def command_cinesDeVerano(m):
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	cadenaCines = cinesDeVerano()
	bot.send_message(cid, cadenaCines, parse_mode='HTML')

bot.polling()


