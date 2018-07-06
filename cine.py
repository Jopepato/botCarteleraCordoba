import re
from bs4 import BeautifulSoup


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