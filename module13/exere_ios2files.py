#!/usr/bin/python

import os
import getopt
import sys
import sqlite3
import shutil

from modules.artfile import logo, header, usage

class bbdd(object):
	"""
    clase bbdd, recibe la ruta a una base de datos
    y crea una lista con los registros con los id,nombre,telefono
    IMPORTANTE LA BASE DE DATOS DEBE EXISTIR SI QUEREMOS USAr generar_lista()
    """


	def __init__(self, bd):
		self.bd = bd
		self.rel_path = os.path.dirname(os.path.relpath(bd))
		if self.rel_path == "":
			self.rel_path = "."
		self.property_paths = ["AppDomain","AppDomainPlugin","AppDomainGroup","SysContainerDomain","SysSharedContainerDomain"]

	def get_bd(self):
		return self.__bd

	def set_bd(self, value):
		self.__bd = value

	def del_bd(self):
		del self.__bd

	def get_rel_path(self):
		return self.rel_path

	bd = property(get_bd, set_bd, del_bd, "la ruta a la base de datos")

	def copy_file(self, hash, file_name):
		"""extrae el fichero del backup con su hash y lo copia en su sitio"""

		oldpath = self.rel_path + "/" + hash[0:2] + "/" + hash
		s = file_name.split('-')
		if (s[0] in self.property_paths):
			newpath = self.rel_path + "/root/" + s[0] + "/" + file_name
		else:
			newpath = self.rel_path + "/root/" + file_name
		if os.path.exists(oldpath):
			shutil.copy(oldpath,newpath)
		else:
			os.makedirs(newpath)


	def generate_list(self):
		"""abre la base de datos y genera la lista de registros"""
		con = sqlite3.connect(self.bd)
		cursor = con.cursor()
		sql = """
			SELECT fileID, domain, relativePath
			FROM Files
			ORDER BY domain, relativePath
		"""
		cursor.execute(sql)
		for i in cursor:
			yield i
			#print (i)

	def generate_csv(self, lista):
		"""exporta a csv la lista que pasamos en el fichero salida, retorna la ruta de salida"""
		s = ''
		salida = self.get_rel_path() + "/" + "tree_names.csv"
		for i in lista:
			#st = i[2].split('/')
			#newpath = os.path.join(i[1],st)
			hash = str(i[0])
			name_path = str(i[1] + "/" + i[2])
			#s = s + str(i[0]) + ";" + i[1] + "/" + i[2] + "\n"
			self.copy_file(hash,name_path)
			s = s + str(hash + ";" + name_path + "\n")

		f = open(salida,"w")
		f.write(s)
		return salida



if __name__ == "__main__":

	logo()
	header()
	name_bd = ""
	try:
		options, arguments = getopt.getopt(sys.argv[1:], "ho:f:")
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	for option, argument in options:
		if option in ('-h'):
			usage()
		elif option == '-f':
			name_bd = argument

    # COMPROBACION DEL FICHERO A PROCESAR

	if name_bd == "":
		print ("error 1: need file ")
		usage()

	if not os.path.exists(name_bd):
		print ("error 2: file %s not found" % name_bd)
		usage ()

	bd = bbdd(name_bd)
	#bd.generate_list()
	print("Work path: " + bd.get_rel_path())
	print("New path of output results will be: " + bd.get_rel_path() + "/root")
	print("Please wait, this process may take a few minutes...")
	error = bd.generate_csv(bd.generate_list())
	print("A results file has been generated: " + error)
