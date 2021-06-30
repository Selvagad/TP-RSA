import primesieve
from os import path,remove
import base64
from maths_utils import *

def encode_stringB64(msg):
    message_bytes = msg.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def decode_stringB64(msg):
    base64_bytes = msg.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')

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

def crypt(keyFile):
    # calculer la taille de n'-1 pour avoir la taille des blocs par ex n'= 6254 donc taille de bloc = 3
    # et pour le dernier bloc je mets des zéros pour remplir
    # donc on crypt de D vers G je crois
    f = open(keyFile, "r")
    if ".pub" in keyFile:
        keyFile = keyFile[0: -4]
    if(f.readline() == "---begin {} public key---\n".format(keyFile)):
        decode_msg = decode_stringB64(f.readline())
        splitted = decode_msg.split('\n')
        n = int(splitted[0], 16)
        e = splitted[1]
        blocSize = len(str(n))
        print(blocSize)
    else:
        print("Le fichier de clé publique n'est pas bon")
    f.close()

def getKeyFromFile(keyFile, fileType):
    if(fileType == 'pub'):
        if(".pub" not in keyFile):
            raise Exception("Mauvais fichier de clé fourni")
        else:
            f = open(keyFile, "r")
            keyFile = keyFile[0: -4]
            if(f.readline() == "---begin {} public key---\n".format(keyFile)):
                return (f.readline().split('\n')[0])
            else:
                print("PB ouverture fichier clé")
    elif(fileType == 'priv'):
        if(".priv" not in keyFile):
            raise Exception("Mauvais fichier de clé fourni")
        else:
            f = open(keyFile, "r")
            keyFile = keyFile[0: -5]
            if(f.readline() == "---begin {} private key---\n".format(keyFile)):
                return (f.readline().split('\n')[0])
            else:
                print("PB ouverture fichier clé")
    f.close()

def encrypt(key, string):
    enc = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(string[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    print(base64.urlsafe_b64encode("".join(enc).encode()).decode())
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decrypt(key, string:str):
    dec = []
    enc = base64.urlsafe_b64decode(string).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    print("".join(dec))
    return "".join(dec)