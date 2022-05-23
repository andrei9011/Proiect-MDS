from numpy import block
from Clasa_Block import Block
from Chain import BlockChain
from Wallet import Wallet
from Transaction import Transaction
from Crypto.Hash import SHA
import binascii
from tkinter import *

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
    # print(nr)
    if (blockchain.blocks[nr-1].transactionCount == 3 or nr == 1):
        blockchain.add_pool_of_data('S-au minat 100 de peepeecoin \n')
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

walletDictionary = {'andrei' : 0, 'alex' : 1, 'ciprian' : 2}
walletList = [alex, andrei, ciprian]

def adaugaTranzactie():
    payer = clicked1.get()
    payee = clicked2.get()
    suma = int(textField.get())

    addTransaction(blockchain, suma, walletList[walletDictionary[payer]], walletList[walletDictionary[payee]])

def afiseazaWalleturi():
    label1 = Label(root, text = 'Ciprian: \n' + ciprian.print_wallet())
    label2 = Label(root, text = 'Andrei: \n' + andrei.print_wallet())
    label3 = Label(root, text = 'Alex: \n' + alex.print_wallet())

    label1.grid(row = 5, column = 1)
    label2.grid(row = 6, column = 1)
    label3.grid(row = 7, column = 1)

def afisareBlockChain():
    label1 = Label(root, text = blockchain.blocks)

    label1.grid(row = 9, column = 1)



root = Tk()
root.title('Blockchain MDS')

textField = Entry(root)
textField.grid(row = 0, column = 2)

clicked1 = StringVar()
clicked2 = StringVar()
clicked1.set("Alege wallet din care se face plata")
clicked2.set("Alege wallet in care se face plata")

drop = OptionMenu(root, clicked1, "andrei", "ciprian", "alex")
drop2 = OptionMenu(root, clicked2, "andrei", "ciprian", "alex")
drop.grid(row = 0, column = 0)
drop2.grid(row = 0, column = 1)

button = Button(root, text = "Efectuati plata", command = adaugaTranzactie)
button2 = Button(root, text = "Afisati walleturi", command = afiseazaWalleturi)
button3 = Button(root, text = "Afisati blockchain", command = afisareBlockChain)
button.grid(row = 2, column = 1)
button2.grid(row = 4, column = 1)
button3.grid(row = 8, column = 1)

root.mainloop()
