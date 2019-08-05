#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import subprocess
import sys

def logo():
	print ("""
            ▓█████    ▒██   ██▒   ▓█████     ██▀███     ▓█████
            ▓█   ▀    ▒▒ █ █ ▒░   ▓█   ▀    ▓██ ▒ ██▒   ▓█   ▀
            ▒███      ░░  █   ░   ▒███      ▓██ ░▄█ ▒   ▒███
            ▒▓█  ▄     ░ █ █ ▒    ▒▓█  ▄    ▒██▀▀█▄     ▒▓█  ▄
            ░▒████▒   ▒██▒ ▒██▒   ░▒████▒   ░██▓ ▒██▒   ░▒████▒
            ░░ ▒░ ░   ▒▒ ░ ░▓ ░   ░░ ▒░ ░   ░ ▒▓ ░▒▓░   ░░ ▒░ ░
             ░ ░  ░   ░░   ░▒ ░    ░ ░  ░     ░▒ ░ ▒░    ░ ░  ░
               ░       ░    ░        ░        ░░   ░       ░
        """)
def header():
	print("""
            EXERE Open Source Project
            Module 14: exere_fix_adb
            This is an ad-hoc solution for fix your smartphone
            detection if crossing adb failed or not recognize
            telegram: @nomed1 @JarkC
        """)

def add_device(vendor,product):
    """Agrega el dispositivo a udev"""
    try:
        f=open('/etc/udev/rules.d/51-android.rules','a')
    except IOError as msg:
        #print msg #descomentar esta linea si queremos ver el mensaje real
        print "ERROR try with: sudo python", sys.argv[0]
        sys.exit(1)

    f.write("SUBSYSTEM==\"usb\", ATTR{idVendor}==\"")
    f.write(str(vendor))
    f.write("\", ATTR{idProduct}==\"")
    f.write(str(product))
    f.write("\", MODE=\"0660\", GROUP=\"plugdev\", SYMLINK+=\"android%n\"")
    f.write("\n")
    f.close()

def get_list_phones():
    """Devuelve la lista de dispositivos de la orden lsusb"""
    df = subprocess.check_output("lsusb")
    devices = []
    for i in df.split('\n'):
        if i: #comprobamos que no esta vacia esa linea
            devices.append(i)
    return devices

def get_vendor(s):
    """Devuelve el idVendor de la linea del dispostivo que pasamos"""
    vector = s.split()
    target = vector[5].split(':') #el campo 5 contine vendor:product
    return target[0]

def get_product(s):
    """Devuelve el idProduct de la linea del dispostivo que pasamos"""
    vector = s.split()
    target = vector[5].split(':') #el campo 5 contine vendor:product
    return target[1]
if __name__ == "__main__":

    logo()
    header()

    devices = get_list_phones()
    cont = 0
    for i in devices:
        print cont,"-",i
        cont = cont + 1
    n1 = int(input("\nChoose number of your smartphone: "))
    n2 = int(input("\nReinsert number to confirm: "))
    if n1 == n2:
        #print get_vendor(devices[n2])
        #print get_product(devices[n2])
        add_device(get_vendor(devices[n2]),get_product(devices[n2]))
    else:
        print "Nothing to do!!"
