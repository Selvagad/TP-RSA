#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import KeysView
from maths_utils import *
from crypto_utils import *
from os import path,remove

from mpmath.functions.functions import re

def checkForSSwitch():
    #check if there is something after the switch
    if("-s" in sys.argv):
        try:
            keySize = sys.argv[sys.argv.index("-s")+1]
            return keySize
        except:
            raise Exception("Erreur: switch s manque paramètre")
    else:
        return 10

def checkForISwitch(method):
    #check if there is something after the switch
    if("-i" in sys.argv):
        try:
            file = sys.argv[sys.argv.index("-i")+1]
            if (method == "encrypt"):
                f = open(file, "r")
                txt = f.readline()
                f.close()
                if(txt == ""):
                    raise Exception("Erreur: le fichier du texte à chiffrer est vide")
                else:
                    return txt
            else:
                f = open(file, "r")
                txt = f.readline()
                f.close()
                if(txt == ""):
                    raise Exception("Erreur: le fichier du texte à déchiffrer est vide")
                else:
                    return txt
        except:
            raise Exception("Erreur: switch i manque paramètre")
    else:
        return 10

# Main()
try :
    #============= Params Management =============
    if len(sys.argv) == 1 or sys.argv[1] == 'help':
        raise Exception()
    elif ((sys.argv[1] == "crypt" or sys.argv[1] == "decrypt") and len(sys.argv) < 4):
        print("Il faut saisir la clé et le texte")
        raise Exception()
    elif (sys.argv[1] == 'keygen'):
        for element in sys.argv:
            if(element == '-f'):
                index = sys.argv.index(element)
                # Check if there is the name for the key file
                if(len(sys.argv) <= index+1 ):
                    sizeKeygen = checkForSSwitch()
                    print(sizeKeygen)
                    n,e,d = computeCoefs(sizeKeygen)
                    createFiles(None, n, e, d)
                #============= Generate keys ===============
                else:
                    sizeKeygen = checkForSSwitch()
                    print("La taille de la clé est: ",sizeKeygen)
                    n,e,d = computeCoefs(sizeKeygen)
                    createFiles(sys.argv[index+1], n, e, d)
    else:
        if(sys.argv[1] == "crypt" and sys.argv[2] != ""):
            encrypt(getKeyFromFile(sys.argv[2], "pub"),checkForISwitch("encrypt"))
        elif (sys.argv[1] == "decrypt" and sys.argv[2] != ""):
            decrypt(getKeyFromFile(sys.argv[2], "priv"),checkForISwitch("decrypt"))
        else:
            raise Exception("Erreur: Vérifier la syntaxe")



except Exception as exc:
    print('\033[91m',exc,'\033[0m')
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    print('\nScript monRSA par Adam Selvaggio\nSyntaxe :')
    print('\t\033[1mmonRSA\033[0m <commande> [<clé>] [<texte>] [switchs]\n')
    print('Commande :\n\tkeygen : Génére une paire de clé\n\tcrytp : Chiffre <texte> pour la clé publique <clé>\n\tdecrytp: Déchiffre <texte> pour la clé privée <clé>\n\thelp : Affiche ce manuel')
    print('Clé :\n\tUn fichier qui contient une clé publique monRSA ("crypt") ou une clé privée ("decrypt")')
    print('Texte :\n\tUne phrase en clair ("crypt") ou une phrase chiffrée ("decrypt")')
    print('Switchs\n\t-f <file> permet de choisir le nom des clé générés, monRSA.pub et monRSA.priv par défaut')
    print('\t-s <size> permet de définir la taille')
    exit(1)