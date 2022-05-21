import collections
import datetime


class Transaction():
    def __init__(self, amount, payer, payee): # constructor de initializare
        self.amount = amount
        self.payer = payer  #public key (hash)
        self.payee = payee  #public key (hash)
        self.time = datetime.datetime.now()

    def make_dict(self):
        return collections.OrderedDict({
            'amount' : self.amount,
            'payer' : self.payer,
            'payee' : self.payee,
            'time' : self.time
        })

    def print_transaction(self):
        transaction = self.make_dict()
        print(f"Amount: ", transaction['amount'], "\nPayer: ",
              transaction['payer'], "\nPayee: ", transaction['payee'],
                                 "\nTime: ", transaction['time'])