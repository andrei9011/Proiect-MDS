from Clasa_Block import Block
from Chain import BlockChain
from Wallet import Wallet
from Transaction import Transaction

#chain = BlockChain(20)


# for i in range (5):
#     data = input("Adauga ceva: ")
#     chain.add_pool_of_data(str(data))
#     chain.mine()
#     block = Block.__new__(Block)
#     if i > 0:
#         block.get_block(chain.blocks[i-1])
#         print(block)
#     print(chain.blocks[i])

alex = Wallet()
andrei = Wallet()
ciprian = Wallet()

print(alex.identity)
print(andrei.identity)
print(ciprian.identity)

transaction1 = Transaction(20, alex.publicKey, ciprian.identity)
transaction2 = Transaction(10, andrei.publicKey, ciprian.identity)
transaction3 = Transaction(5, andrei.publicKey, alex.identity)

signature1 = alex.make_a_payement(5,andrei.identity)
signature2 = ciprian.make_a_payement(10,andrei.identity)
signature3 = andrei.make_a_payement(5,alex.identity)

print(signature1, "\n", signature2, "\n", signature3)
