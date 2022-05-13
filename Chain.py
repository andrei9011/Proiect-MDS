import hashlib

from Clasa_Block import Block


class BlockChain():
    def __init__(self, diff):
        self.diff = diff
        self.blocks = []
        self.data_pool = []
        self.create_origin_block()

    def verify_diff_hash(self, block):
        hash = hashlib.sha256()
        hash.update(str(block).encode('utf-8'))
        return block.hash.hexdigest() == hash.hexdigest() and int(hash.hexdigest(), 16) < 2 ** (256-self.diff) and block.previous_hash == self.blocks[-1].hash

    def add_block(self, block):
        if self.verify_diff_hash(block):
            self.blocks.append(block)

    def add_pool_of_data(self, data):
        self.data_pool.append(data)

    def create_origin_block(self):
        hash = hashlib.sha256()
        hash.update(''.encode('utf-8'))
        origin = Block("Origin", hash)
        origin.mine(self.diff)
        self.blocks.append(origin)

    def mine(self):
        if len(self.data_pool):
            data = self.data_pool.pop()
            block = Block(data, self.blocks[-1].hash)
            block.mine(self.diff)
            self.add_block(block)
