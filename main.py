#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

def calcul():
    print("toto")

#create .pub and .priv files
def createFiles(filename):
    if(filename == None):
        print("monRSA.pub")
    else:
        print(filename)

# Main()
try :
    #============= Params Management =============
    if len(sys.argv) == 1 or sys.argv[1] == 'help':
        exit(1)
    elif ((sys.argv[1] == "crypt" or sys.argv[1] == "decrypt") and len(sys.argv) < 4):
        print("Il faut saisir la clé et le texte")
        exit(1)
    elif (sys.argv[1] == 'keygen'):
        for element in sys.argv:
            if(element == '-f'):
                index = sys.argv.index(element)
                # Check if there are enough parameters
                if(len(sys.argv) <= index+1 ):
                    createFiles(None)
                else:
                    createFiles(sys.argv[index+1])


except:
    print('\nScript monRSA par Adam Selvaggio\nSyntaxe :')
    print('monRSA <commande> [<clé>] [<texte>] [switchs]')
    print('Commande :\n\tkeygen : Génére une paire de clé\n\tcrytp : Chiffre <texte> pour le clé publique <clé>\n\tdecrytp: Déchiffre <texte> pour le clé privée <clé>\n\thelp : Affiche ce manuel')
    print('Clé :\n\tUn fichier qui contient une clé publique monRSA ("crypt") ou une clé privée ("decrypt")')
    print('Texte :\n\tUne phrase en clair ("crypt") ou une phrase chiffrée ("decrypt")')
    print('Switchs\n\t-f <file> permet de choisir le nom des clé générés, monRSA.pub et monRSA.priv par défaut')
    exit(1)