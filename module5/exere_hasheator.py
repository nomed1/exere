#!/usr/bin/python

import os
import sys
import time
import getopt
import hashlib as hash

def genhash(fichero):
	""" generate hash of file fichero"""
	TAM = 65536	
	sha = hash.sha256()
	with open(fichero, 'rb') as f:
		buf = f.read(TAM)
		while len(buf) > 0:
			sha.update(buf)
			buf = f.read(TAM)
	return sha.hexdigest()

def appendhash(hash,fichero,hashfile):
	""" add hash to the file hashfile with the name of file fichero"""
	f = open(hashfile, "a")
	f.write(hash + ',' + fichero + '\n')
	f.close()

def recorrer(carpeta):
	"""hashing recursively all files in folder carpeta and add to hash's file"""
	lista = os.listdir(carpeta)
	#print (lista)
	for elemento in lista:
		nuevo = os.path.join(carpeta,os.path.basename(elemento))
		if os.path.isdir(nuevo):
			recorrer(nuevo)			
		else:
			destino = os.path.join(os.getcwd(),pathDestino)
			print("hashing ", nuevo)
			appendhash(genhash(nuevo).upper(), nuevo, filehash)

	
def logo():
    print("""
            ▓█████    ▒██   ██▒   ▓█████     ██▀███     ▓█████ 
            ▓█   ▀    ▒▒ █ █ ▒░   ▓█   ▀    ▓██ ▒ ██▒   ▓█   ▀ 
            ▒███      ░░  █   ░   ▒███      ▓██ ░▄█ ▒   ▒███   
            ▒▓█  ▄     ░ █ █ ▒    ▒▓█  ▄    ▒██▀▀█▄     ▒▓█  ▄ 
            ░▒████▒   ▒██▒ ▒██▒   ░▒████▒   ░██▓ ▒██▒   ░▒████▒
            ░░ ▒░ ░   ▒▒ ░ ░▓ ░   ░░ ▒░ ░   ░ ▒▓ ░▒▓░   ░░ ▒░ ░
             ░ ░  ░   ░░   ░▒ ░    ░ ░  ░     ░▒ ░ ▒░    ░ ░  ░
               ░       ░    ░        ░        ░░   ░       ░   
        """)
def cabecera():
    print("""
            EXERE Open Source Project
            Modulo 5:
            Calculate checksum sha2(256) all files recursively in a folder
            telegram @nomed1 - xpressmoviles@gmail.com
            www.eltallerdelosandroides.com
            
            
        """)

def uso ( ):
    print ('Usage: %s [options] -d <folder>\n' % sys.argv[0])
    print ("""
            Options:
            -h               see this help
            -d <folder>     folder to process
            
            Note: report file will be hashed
            """)
    sys.exit(1)
    
if __name__ == "__main__":
    
    logo()
    cabecera()

    bd = ""
    try:                                
        opciones, argumentos = getopt.getopt(sys.argv[1:], "ho:d:")
    except getopt.GetoptError:          
        uso()                         
        sys.exit(2)

    for opcion, argumento in opciones:                
        if opcion in ('-h'):
            uso()                   
        elif opcion == '-d':                
            bd = argumento

    # CHECK TO PROCESS
    
    if bd == "":
        print ("error, folder not found")
        uso()

    if not os.path.exists(bd):
        print ("error: folder %s not found" % bd)
        uso ()
		
    if not os.path.isdir(bd):
        print ("error, argument %s is not a folder" % bd)
        uso()
	
	# GO
	
    ahora = time.strftime("%Y%m%d_%H%M%S")
    pathActual = os.getcwd()
    pathDestino = os.path.join(pathActual,ahora)
	
    filehash = os.path.join(pathActual,ahora + ".csv")
    print("All hashes will be save in\n", filehash, "\n")
	
    recorrer(bd)
    appendhash(genhash(filehash).upper(),ahora + ".csv",filehash + ".sha256")