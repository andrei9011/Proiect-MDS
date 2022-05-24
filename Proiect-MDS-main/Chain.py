import hashlib

from Clasa_Block import Block

class BlockChain():
    def __init__(self, diff): # constructor de initializare al unui block chain in care se va crea si blockul de origine
        self.diff = diff
        self.blocks = []
        self.data_pool = []
        self.create_origin_block()

    def verify_diff_hash(self, block): #verificare pentru difficulty ca sa rezulte nonce-ul diferit
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2 ** (256-self.diff) and block.previous_hash == self.blocks[-1].hash

    def add_block(self, block): # adaugare de blockuri in chain
        if self.verify_diff_hash(block):
            self.blocks.append(block)

    def add_pool_of_data(self, data): # adaugare de date noi in chain
        self.data_pool.append(data)

    def create_origin_block(self): # creare block origine
        hash = hashlib.sha256()
        hash.update(''.encode('utf-8'))
        origin = Block("Origin", hash)
        origin.mine(self.diff)
        self.blocks.append(origin)

    def mine(self): # metoda de minare si creare de blockuri noi
        if len(self.data_pool):
            data = self.data_pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.diff)
            self.add_block(block)
