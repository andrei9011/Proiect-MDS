import hashlib

from Clasa_Block import Block

class BlockChain():
    def __init__(self,diff):
        self.diff = diff
        self.blocks = []
        self.data_pool = []

    def verify_diff_hash(self, block):
        hash = hashlib.sha256()
        h.update(str(block).encode('utf-8'))
        return block.h.hexdigest() == h.hexdigest() and int(h.hexdigest(), 16) < 2**(256-self.diff)

    def add_block(self, block):
        if self.verify_diff_hash(block):
            self.blocks.append(block)

    def add_pool_of_data(self, data):
        self.data_pool.append(data)

    def create_origin_block(self):
        h = hashlib.sha256()
        h.update(''.encode('utf-8'))
        origin = Block("Origin",h)
        origin.mine(self.diff)
        self.blocks.append(origin)

    def mine(self):
        if len(self.pool):
            data = self.data_pool.pop()
            block = Block(data,self.blocks[-1].hash)
            block.mine(self.diff)
            self.add_block(block)



