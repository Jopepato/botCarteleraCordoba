import requests
import re
import imdb
from bs4 import BeautifulSoup
from cine import Cine
from cinemaNames import *

def encuentraDatosCine(cinemaName):

    #Query the website and return the html to the variable 'page'
    response = requests.get(CARTELERANAME)
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            return False

        auxCine = Cine()

        for i in soup.find_all(id='bloqueportadaa'):
            auxCine.setNombreCine(i.h1.string)
            listaPeliculasAux = []
            listaHorariosAux = []
            if cinemaName == auxCine.getNombreCine():
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
    else:
        return False

def cinesDeVerano():
    #Esto va a devolver la cadena ya directa con los cines de veranO

    #Query the website and return the html to the variable 'page'
    response = requests.get(CARTELERANAME)
    if response.status_code == 200:

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
        except Exception as e:
            return False
        
        cadenaCinesDeVerano = ''
        auxCine = Cine()
        for i in soup.find_all(id='bloqueportadaa'):
            auxCine.nombreCine_ = str(i.h1.string)
            listaPeliculasAux = []
            listaHorariosAux = []
            if auxCine.getNombreCine() == SANANDRESNAME or auxCine.getNombreCine() == OLIMPIANAME or auxCine.getNombreCine() == FUENSECANAME or auxCine.getNombreCine() == DELICIASNAME or auxCine.getNombreCine() == PLAZADETOROSNAME:
                for j in i.find_all('div', class_='pildora'):
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
                cadenaCinesDeVerano = cadenaCinesDeVerano + "<b>" + auxCine.getNombreCine() + "</b>" + '\n'
                p = 0
                for q in auxCine.getNombrePeliculas():
                    #Tenemos que encontrar el id de la pelicula y pasar el titulo
                    movieID = getMovieID(q)
                    if movieID != "":
                        cadenaCinesDeVerano = cadenaCinesDeVerano + '<a href="' + IMDBTITLE + movieID + '">' + q + '</a>' + '\n'
                    else:
                        cadenaCinesDeVerano = cadenaCinesDeVerano + '<b>' + q + '</b>' + '\n'
                    cadenaCinesDeVerano = cadenaCinesDeVerano + "<i>" + auxCine.horarioPeliculas_[p] + "</i>" + '\n'
                    p = p+1
                cadenaCinesDeVerano = cadenaCinesDeVerano + '\n'

        return cadenaCinesDeVerano
    else:
        return False

def daFormatoCadena(cine):
    #Con esta funcion nos viene un objeto de la clase cine e intentamos montar una cadena que no quede mal
    cadena = "<b>" + cine.getNombreCine() + "</b>" + '\n\n'
    j=0
    for i in cine.getNombrePeliculas():
        movieID = getMovieID(i)
        cadena = cadena + '<a href="' + IMDBTITLE + movieID + '">' + i + '</a>' + '\n'
        cadena = cadena + "<i>" + cine.horarioPeliculas_[j] +"</i>" + '\n\n'
        j = j+1
    return cadena

def getMovieID(movieName):
    ia = imdb.IMDb()
    try:
        movies = ia.search_movie(movieName)
    except IOError as e:
        return ""

    return movies[0].movieID