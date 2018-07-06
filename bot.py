#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import telebot
from time import sleep
from functions import cinesDeVerano, encuentraDatosCine, daFormatoCadena
from cinemaNames import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

TOKEN = '330883133:AAHvkTpcFu8Z-0XR8JmfUsppRqL6BWTBSII' # Nuestro tokken del bot (el que @BotFather nos dió).
bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

#Funciones
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hey, ve pillando palomitas que nos vamos al cine.")
	print "[" + str(message.chat.id) + "]: " + message.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 

@bot.message_handler(commands=['tablero']) # Indicamos que lo siguiente va a controlar el comando '/roto2'.
def command_cineTablero(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    #Tenemos que coger el cine y devolveremos los horarios que queremos
    horarios = encuentraDatosCine(TABLERONAME)
    #horarios.printTotal()
    mensajeDevuelta= daFormatoCadena(horarios)
    bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')
    #Vamos a intentar parsear un poco el mensaje


@bot.message_handler(commands=['guadalquivir']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_cineGuadalquivir(m): # Definimos una función que resuleva lo que necesitemos.
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	horarios = encuentraDatosCine(GUADALQUIVIRNAME)
	mensajeDevuelta= daFormatoCadena(horarios)
	bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')

@bot.message_handler(commands=['lucena'])
def command_cineLucena(m):
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	horarios = encuentraDatosCine(LUCENANAME)
	mensajeDevuelta= daFormatoCadena(horarios)
	bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')

@bot.message_handler(commands=['cinesDeVerano'])
def command_cinesDeVerano(m):
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	cadenaCines = cinesDeVerano()
	bot.send_message(cid, cadenaCines, parse_mode='HTML')

bot.polling()