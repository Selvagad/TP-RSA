#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from maths_utils import *
from crypto_utils import *

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
                # Check if there are enough parameters
                if(len(sys.argv) <= index+1 ):
                    n,e,d = computeCoefs()
                    createFiles(None, n, e, d)
                #============= Generate keys ===============
                else:
                    n,e,d = computeCoefs()
                    createFiles(sys.argv[index+1], n, e, d)
    else:
        if(sys.argv[1] == "crypt" and sys.argv[2] != ""):
            encrypt(getKeyFromFile(sys.argv[2], "pub"),sys.argv[3])
        elif (sys.argv[1] == "decrypt" and sys.argv[2] != ""):
            decrypt(getKeyFromFile(sys.argv[2], "priv"),sys.argv[3])
        else:
            raise Exception("Erreur: Vérifier la syntaxe")



except Exception as exc:
    print('\033[91m',exc,'\033[0m')
    print('\nScript monRSA par Adam Selvaggio\nSyntaxe :')
    print('\t\033[1mmonRSA\033[0m <commande> [<clé>] [<texte>] [switchs]\n')
    print('Commande :\n\tkeygen : Génére une paire de clé\n\tcrytp : Chiffre <texte> pour la clé publique <clé>\n\tdecrytp: Déchiffre <texte> pour la clé privée <clé>\n\thelp : Affiche ce manuel')
    print('Clé :\n\tUn fichier qui contient une clé publique monRSA ("crypt") ou une clé privée ("decrypt")')
    print('Texte :\n\tUne phrase en clair ("crypt") ou une phrase chiffrée ("decrypt")')
    print('Switchs\n\t-f <file> permet de choisir le nom des clé générés, monRSA.pub et monRSA.priv par défaut\n')
    exit(1)