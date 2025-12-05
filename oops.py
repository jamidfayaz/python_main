class account:
    bank_name="jamid's bank"
    print("welcome to my bank")

    def __init__(self,name,age,balance):            #constructor by dunder method
        self.name=name
        self.age=age
        self.balance=balance
    
    def deposit(self,amount):           #methods
        self.balance=self.balance+amount
        print(self.balance)
    def withdraw(self,amount):
        self.balance=self.balance-amount

client_1=account("jamid",25,200000)         #passing arg     we use self bcz #account.name(client_1)
client_1.address="dehrana"     #locally adding data to object

client_2=account("aqib",23,100000)

client_1.deposit(5000)
print(client_1.bank_name)
print(client_1.name)
print(client_1.address)