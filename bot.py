#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import telebot
from time import sleep
from functions import cinesDeVerano, encuentraDatosCine, daFormatoCadena
from cinemaNames import *
from private import TOKEN
import sys

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
logger = logging.getLogger('botLogger')
logger.setLevel(logging.ERROR)
#Funciones
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hey, ve pillando palomitas que nos vamos al cine.")
	#print '[' + str(message.chat.id) + ']: ' + message.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start
 

@bot.message_handler(commands=['tablero']) # Indicamos que lo siguiente va a controlar el comando '/roto2'.
def command_cineTablero(m): # Definimos una función que resuelva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    #Tenemos que coger el cine y devolveremos los horarios que queremos
    datosCine = encuentraDatosCine(TABLERONAME)
    if datosCine:
        mensajeDevuelta= daFormatoCadena(datosCine)
        bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')
    else:
        bot.send_message(cid, 'Something went wrong', parse_mode='HTML')


@bot.message_handler(commands=['guadalquivir']) # Indicamos que lo siguiente va a controlar el comando '/miramacho'
def command_cineGuadalquivir(m): # Definimos una función que resuleva lo que necesitemos.
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    #bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    datosCine = encuentraDatosCine(GUADALQUIVIRNAME)
    if datosCine:
        mensajeDevuelta= daFormatoCadena(datosCine)
        bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')
    else:
        bot.send_message(cid, 'Something went wrong', parse_mode='HTML')

@bot.message_handler(commands=['lucena'])
def command_cineLucena(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    #bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
    datosCine = encuentraDatosCine(LUCENANAME)
    if datosCine:
        mensajeDevuelta= daFormatoCadena(datosCine)
        bot.send_message(cid, mensajeDevuelta, parse_mode='HTML')
    else:
        bot.send_message(cid, 'Something went wrong', parse_mode='HTML')

@bot.message_handler(commands=['cinesDeVerano'])
def command_cinesDeVerano(m):
	cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
	#bot.send_message( cid, 'Vete a la mierda') # Con la función 'send_message()' del bot, enviamos al ID almacenado el texto que queremos.
	cadenaCines = cinesDeVerano()
	bot.send_message(cid, cadenaCines, parse_mode='HTML')

try:

    bot.polling(none_stop=True)

# ConnectionError and ReadTimeout because of possible timout of the requests library

# TypeError for moviepy errors

# maybe there are others, therefore Exception

except Exception as e:

    logger.error(e)