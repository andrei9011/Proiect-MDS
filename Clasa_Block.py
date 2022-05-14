import hashlib

class Block():
    def __init__(self, data, previous_hash): #constructor de initializare
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.data = data

    def __new__(cls, *args, **kwargs): #creare de obiect nou fara atribuire de date
        return super().__new__(cls)

    def get_block(self, block):  #getter
        self.hash = block.hash
        self.previous_hash = block.previous_hash
        self.nonce = block.nonce
        self.data = block.data

    def mine(self, difficulty): #procesul de minare
        self.hash.update(str(self).encode('utf-8'))
        while int(self.hash.hexdigest(), 16) > 2 ** (256 - difficulty):
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def __str__(self): # metoda de printare pentru un block
        return "{}{}{}".format(self.previous_hash.hexdigest(), self.data, self.nonce)
