from Chain import BlockChain

chain = BlockChain(5)

for i in range (5):
    data = input("Adauga ceva: ")
    chain.add_pool_of_data(str(i))
    chain.mine()