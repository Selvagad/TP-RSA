#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import primesieve
from maths_utils import *
from os import path,remove
import base64

def encode_stringB64(msg):
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

#create .pub and .priv files
def createFiles(filename, n, e, d):
    if(filename == None):
        writeInFile(None, n, e, d)
    else:
        filepath = filename+".pub"
        writeInFile(filepath, n, e, d)

def writeInFile(filename, n, e, d):
    if(filename == None):
        # Generate public key file
        txt = hex(n)+"\n"+hex(e)
        f = open("monRSA.pub", "w")
        f.write("---begin monRSA public key---\n")
        f.write(encode_stringB64(txt)+"\n")
        f.write("---end monRSA key---\n")
        f.close()
        #Generate private key file
        txt = hex(n)+"\n"+hex(d)
        f = open("monRSA.priv", "w")
        f.write("---begin monRSA private key---\n")
        f.write(encode_stringB64(txt)+"\n")
        f.write("---end monRSA key---\n")
        f.close()
    else:
        # Generate public key file
        txt = hex(n)+"\n"+hex(e)
        f = open(filename, "w")
        f.write("---begin {} public key---\n".format(filename[0: -4]))
        f.write(encode_stringB64(txt)+"\n")
        f.write("---end {} key---\n".format(filename[0: -4]))
        f.close()
        #Generate private key file
        txt = hex(n)+"\n"+hex(d)
        f = open(filename, "w")
        f.write("---begin {} private key---\n".format(filename[0: -4]))
        f.write(encode_stringB64(txt)+"\n")
        f.write("---end {} key---\n".format(filename[0: -4]))
        f.close()

def computeCoefs():
    p = primesieve.n_primes(1, random.randint(1000000000, 10000000000-1))[0]
    q = primesieve.n_primes(1, random.randint(1000000000, 10000000000-1))[0]
    n = p*q
    n_prim = (p-1)*(q-1)
    e, d = findFirstED(n_prim)
    print("p=", p)
    print("q=", q)
    print("n=", n)
    print("n\'=", n_prim)
    print("e=", e)
    print("d=", d)
    return n,e,d

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
                    n,e,d = computeCoefs()
                    createFiles(None, n, e, d)
                #============= Generate keys ===============
                else:
                    n,e,d = computeCoefs()
                    createFiles(sys.argv[index+1], n, e, d)


except Exception as exc:
    print(exc)
    print('\nScript monRSA par Adam Selvaggio\nSyntaxe :')
    print('monRSA <commande> [<clé>] [<texte>] [switchs]')
    print('Commande :\n\tkeygen : Génére une paire de clé\n\tcrytp : Chiffre <texte> pour le clé publique <clé>\n\tdecrytp: Déchiffre <texte> pour le clé privée <clé>\n\thelp : Affiche ce manuel')
    print('Clé :\n\tUn fichier qui contient une clé publique monRSA ("crypt") ou une clé privée ("decrypt")')
    print('Texte :\n\tUne phrase en clair ("crypt") ou une phrase chiffrée ("decrypt")')
    print('Switchs\n\t-f <file> permet de choisir le nom des clé générés, monRSA.pub et monRSA.priv par défaut')
    exit(1)