from numpy import block
from Clasa_Block import Block
from Chain import BlockChain
from Wallet import Wallet
from Transaction import Transaction
import Crypto.Cipher.PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5
import Crypto.Random
import Crypto
import binascii

#chain = BlockChain(20)

def make_a_payement(amount, wallet1, wallet2):
    transaction = Transaction(amount, wallet1.publicKey, wallet2.publicKey)
    wallet1.amount = wallet1.amount - amount
    wallet2.amount = wallet2.amount + amount
    hash = SHA.new(str(transaction.make_dict()).encode('utf-8'))
    return binascii.hexlify(wallet1.signer.sign(hash)).decode('ascii')

def addTransaction(blockchain, amount, payer, payee):
    transaction = Transaction(amount, payer.identity, payee.identity)
    signature = make_a_payement(amount, payer, payee)
    blockchain[i].transactionList.append(transaction1)
    gigel.transactionCount = gigel.transactionCount + 1


# for i in range (5):
#     data = input("Adauga ceva: ")
#     chain.add_pool_of_data(str(data))
#     chain.mine()
#     block = Block.__new__(Block)
#     if i > 0:
#         block.get_block(chain.blocks[i-1])
#         print(block)
#     print(chain.blocks[i])

blockchain = BlockChain(20)

gigel = Block("test", blockchain.blocks[0].hash)

alex = Wallet()
andrei = Wallet()
ciprian = Wallet()

print(alex.identity)
print(andrei.identity)
print(ciprian.identity)


transaction2 = Transaction(10, andrei.identity, ciprian.identity)
transaction3 = Transaction(5, andrei.identity, alex.identity)


gigel.transactionList.append(transaction2)
gigel.transactionCount = gigel.transactionCount + 1
gigel.transactionList.append(transaction3)
gigel.transactionCount = gigel.transactionCount + 1


signature2 = make_a_payement(10,andrei, ciprian)
signature3 = make_a_payement(5,alex, ciprian)

transaction1.print_transaction()
transaction2.print_transaction()
transaction3.print_transaction()

print("cati bani are prostul: " + str(alex.amount))
print("cati bani are andrei: " + str(andrei.amount))
print("cati bani are ciprian: " + str(ciprian.amount))
print("signature1: " + str(signature1))
print("signature2: " + str(signature2))
print("gigel transaction count: " + str(gigel.transactionCount))
gigel.transactionList[1].print_transaction()


