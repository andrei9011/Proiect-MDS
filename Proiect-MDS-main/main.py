from Clasa_Block import Block
from Chain import BlockChain
from Wallet import Wallet
from Transaction import Transaction
from Crypto.Hash import SHA
import binascii
from tkinter import *
#sudo apt-get install python3-tk pentru tkinter

def make_a_payement(amount, wallet1, wallet2): #make a payment este o metoda in care se face o tranzactie si se va folosii de semnatura celui care
    transaction = Transaction(amount, wallet1.publicKey, wallet2.publicKey) # a facut plata si tranzactia hash-uita
    wallet1.amount = wallet1.amount - amount
    wallet2.amount = wallet2.amount + amount
    hash = SHA.new(str(transaction.make_dict()).encode('utf-8'))
    return binascii.hexlify(wallet1.signer.sign(hash)).decode('ascii')

def addTransaction(blockchain, amount, payer, payee):# tranzactia va fi adaugata intr-un block daca exista spatiu
    transaction = Transaction(amount, payer.identity, payee.identity) # daca nu exista spatiu se va crea un block nou
    signature = make_a_payement(amount, payer, payee)
    nr = len(blockchain.blocks)
    # print(nr)
    if (blockchain.blocks[nr-1].transactionCount == 3 or nr == 1):
        blockchain.add_pool_of_data('S-au minat 100 de bitcoin (am vrea noi) \n')
        blockchain.mine()
        bloc = Block('', blockchain.blocks[nr-1].hash)
        blockchain.add_block(bloc)
        nr = len(blockchain.blocks)
    blockchain.blocks[nr-1].transactionList.append(transaction)
    blockchain.blocks[nr - 1].transactionCount = blockchain.blocks[nr-1].transactionCount + 1
    blockchain.blocks[nr - 1].data = blockchain.blocks[nr - 1].data + str(signature)[:50] + '\n'

blockchain = BlockChain(20) #blockchain-ul cu difficultatea de 20

#wallet-urile noastre
alex = Wallet()
andrei = Wallet()
ciprian = Wallet()

walletDictionary = {'andrei' : 0, 'alex' : 1, 'ciprian' : 2}
walletList = [andrei, alex, ciprian]

#functie pentru a crea tranzactii prin interfata
def adaugaTranzactie():
    payer = clicked1.get()
    payee = clicked2.get()
    suma = int(textField.get())

    addTransaction(blockchain, suma, walletList[walletDictionary[payer]], walletList[walletDictionary[payee]])

#metoda pentru a afisa wallet-urile prin interfata
def afiseazaWalleturi():
    label1 = Label(root, text = 'Ciprian: \n' + ciprian.print_wallet())
    label2 = Label(root, text = 'Andrei: \n' + andrei.print_wallet())
    label3 = Label(root, text = 'Alex: \n' + alex.print_wallet())

    label1.grid(row = 5, column = 1)
    label2.grid(row = 6, column = 1)
    label3.grid(row = 7, column = 1)

#metoda de a afisa cate un block din blockchain prin interfata
def afisareBlockChain():
    if labelGol['text'] != '':
        labelGol['text'] = ""
    index = int(textField2.get())
    labelGol['text'] = blockchain.blocks[index]
    labelGol.grid(row = 9, column = 1)

#def clearLabel():
 #   root.children.clear()

#root este root-ul pentru tkinter adica window-ul in sine
root = Tk()
root.title('Blockchain MDS')

#label folosit pentru a putea arata blockchain-ul
labelGol = Label(root)

#textField este un textfield pentru suma tranzactiei5
textField = Entry(root)
textField.grid(row = 0, column = 2)

#textfield2 reprezinta care blockchain vrem sa il vedem
textField2 = Entry(root)
textField2.grid(row = 8, column = 2)

#clicked 1 si 2 sunt wallet-urile intre care se efectueaza tranzactia
clicked1 = StringVar()
clicked2 = StringVar()
clicked1.set("Alege wallet din care se face plata")
clicked2.set("Alege wallet in care se face plata")

#dropdown-urile pentru fiecare wallet
drop = OptionMenu(root, clicked1, "andrei", "alex", "ciprian")
drop2 = OptionMenu(root, clicked2, "andrei", "alex", "ciprian")
drop.grid(row = 0, column = 0)
drop2.grid(row = 0, column = 1)

#butoane cu functii diferite precum afisare walleturi efectuare plata si afisare blockchain
button = Button(root, text = "Efectuati plata", command = adaugaTranzactie)
button2 = Button(root, text = "Afisati walleturi", command = afiseazaWalleturi)
button3 = Button(root, text = "Afisati blockchain", command = afisareBlockChain)
#button4 = Button(root, text = "Clear", command = clearLabel)
button.grid(row = 2, column = 1)
button2.grid(row = 4, column = 1)
button3.grid(row = 8, column = 1)
#button4.grid(row = 10, column = 1)

root.mainloop()
