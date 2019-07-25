#!/usr/bin/python

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
            Module 13:
            Expand a copy of a non encryption iTunes backup
            up ios 10 to a readable and navigable structure
            telegram: @nomed1 @JarkC

        """)

def usage ( ):
	print ('Usage: %s [options]\n' % sys.argv[0])
	print ("""
            Options:
            -h               see this help
            -f <file>        pathfile/Manifest.db to process

            Note: all folders XX must be in same path
                  than Manifest.db
            """)
	sys.exit(1)

if __name__ == "__main__":

	logo()
	cabecera()
