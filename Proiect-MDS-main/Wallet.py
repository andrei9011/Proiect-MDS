 #pip3 install pycryptodome
import Crypto.Cipher.PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Random
import Crypto
import binascii
import hashlib
from Transaction import Transaction

class Wallet(): # Clasa wallet pt fiecare utilizator
    def __init__(self):
        self.keyPair = RSA.generate(1024, Crypto.Random.new().read) #se va genera un keypair random folosind RSA (poate functiona si ca un private key)
        self.publicKey = self.keyPair.publickey() # cheia publica
        self.pubKeyPEM = self.publicKey.exportKey() # cheia publica in format PEM pentru a putea fi citit ca string
        self.privateKey =  self.keyPair.exportKey() # cheia privata din acest keypair
        self.signer =  PKCS1_v1_5.new(self.keyPair) # semnatura fiecarui utilizator pentru a putea fi gasita o tranzactie se fol de cheia privata
        self.amount = 100 # suma de bani pe care o are

    @property
    def identity(self): # aceasta este identitatea unui utilizator folosindu-se de cheia publica in format PEM
        return binascii.hexlify(self.pubKeyPEM).decode('ascii')

    def _publickey(self): #metoda pentru a afisa cheia publica in format hexa
        return hex(self.publicKey.n)

    def print_wallet(self): #metoda de printare a atributelor din clasa identitatea este de la 240:290 deoarece acolo incep sa fie diferite valorile
        return ("Amount: " + str(self.amount) + "\n" + "Identity: " + self.identity[240:290])
        