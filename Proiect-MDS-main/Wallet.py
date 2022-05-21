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

class Wallet():
    def __init__(self):
        self.keyPair = RSA.generate(1024, Crypto.Random.new().read)
        self.publicKey = self.keyPair.publickey()
        self.pubKeyPEM = self.publicKey.exportKey()
        self.privateKey =  self.keyPair.exportKey()
        self.signer =  PKCS1_v1_5.new(self.keyPair)
        self.amount = 100 

    @property
    def identity(self):
        return binascii.hexlify(self.pubKeyPEM).decode('ascii')



    def _publickey(self):
        return hex(self.publicKey.n)