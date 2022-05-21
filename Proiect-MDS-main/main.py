from Clasa_Block import Block
from Chain import BlockChain
from Wallet import Wallet
from Transaction import Transaction
from Crypto.Hash import SHA
import binascii

def make_a_payement(amount, wallet1, wallet2):
    transaction = Transaction(amount, wallet1.publicKey, wallet2.publicKey)
    wallet1.amount = wallet1.amount - amount
    wallet2.amount = wallet2.amount + amount
    hash = SHA.new(str(transaction.make_dict()).encode('utf-8'))
    return binascii.hexlify(wallet1.signer.sign(hash)).decode('ascii')

def addTransaction(blockchain, amount, payer, payee):
    transaction = Transaction(amount, payer.identity, payee.identity)
    signature = make_a_payement(amount, payer, payee)
    nr = len(blockchain.blocks)
    print(nr)
    if (blockchain.blocks[nr-1].transactionCount == 3 or nr == 1):
        blockchain.add_pool_of_data('S-a minat 100 de coco \n')
        blockchain.mine()
        bloc = Block('', blockchain.blocks[nr-1].hash)
        blockchain.add_block(bloc)
        nr = len(blockchain.blocks)
    blockchain.blocks[nr-1].transactionList.append(transaction)
    blockchain.blocks[nr - 1].transactionCount = blockchain.blocks[nr-1].transactionCount + 1
    blockchain.blocks[nr - 1].data = blockchain.blocks[nr - 1].data + str(signature) + '\n'

blockchain = BlockChain(20)


alex = Wallet()
andrei = Wallet()
ciprian = Wallet()


addTransaction(blockchain,20,andrei,ciprian)
addTransaction(blockchain,20,andrei,ciprian)
addTransaction(blockchain,20,andrei,ciprian)
addTransaction(blockchain,20,andrei,ciprian)
print(len(blockchain.blocks),andrei.amount,blockchain.blocks[len(blockchain.blocks)-2].data)
print(ciprian.amount)
