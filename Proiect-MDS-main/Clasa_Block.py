import hashlib

class Block():
    def __init__(self, data, previous_hash): #constructor de initializare
        self.hash = hashlib.sha256()
        self.previous_hash = previous_hash
        self.nonce = 0
        self.data = data
        self.transactionList = []
        self.transactionCount = 0

    def __new__(cls, *args, **kwargs): #creare de obiect nou fara atribuire de date
        return super().__new__(cls)

    def get_block(self, block):  #getter
        self.hash = block.hash
        self.previous_hash = block.previous_hash
        self.nonce = block.nonce
        self.data = block.data

    def mine(self, difficulty): #procesul de minare se tot updateaza hash-ul si cat timp valoarea lui in int este mai mare
        self.hash.update(str(self).encode('utf-8')) #decat 2^256- dificultate se va tot itera si se va tot crea un hash nou pana sa se poata crea un
        while int(self.hash.hexdigest(), 16) > 2 ** (256 - difficulty): # nou bloc
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def __str__(self): # metoda de printare pentru un block
        return "previous hash: {}\ndata: {}\nnonce: {}".format(self.previous_hash.hexdigest(), self.data, self.nonce)
