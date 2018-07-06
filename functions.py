import urllib2
import re
from bs4 import BeautifulSoup
from cine import Cine
from cinemaNames import CARTELERANAME


def encuentraDatosCine(cinemaName):

    #Query the website and return the html to the variable 'page'
    page = urllib2.urlopen(CARTELERANAME)

    soup = BeautifulSoup(page, 'html.parser')

    auxCine = Cine()

    for i in soup.find_all(id='bloqueportadaa'):
        auxCine.setNombreCine(i.h1.string)
        listaPeliculasAux = []
        listaHorariosAux = []
        if cinemaName == aux.getNombreCine():
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
            auxCine.setNombrePeliculas(listaPeliculasAux)
            auxCine.setHorarioPeliculas(listaHorariosAux)
            break

    return auxCine

def cinesDeVerano():
	#Esto va a devolver la cadena ya directa con los cines de veranO

	#Query the website and return the html to the variable 'page'
	page = urllib2.urlopen(CARTELERANAME)

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
