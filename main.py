from Clasa_Block import Block
from Chain import BlockChain

chain = BlockChain(20)


for i in range (5):
    data = input("Adauga ceva: ")
    chain.add_pool_of_data(str(data))
    chain.mine()
    block = Block.__new__(Block)
    if i > 0:
        block.get_block(chain.blocks[i-1])
        print(block)
    print(chain.blocks[i])