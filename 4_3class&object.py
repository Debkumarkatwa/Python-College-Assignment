class bank:
    
    def __init__(self,bank_name, name, balance, account_number):
        self.bank_name = bank_name
        self.name = name
        self.balance = balance
        self.acc = account_number
        print(f"{self.name} Welcome to {self.bank_name}.\nYour account number is {self.acc}.")
    
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{self.name}, You Debited {amount} from account {self.acc}.")
    
    def credit(self, amount):
        self.balance += amount
        print(f"{self.name}, You Credited {amount} to account {self.acc}.")

    def update(self):
        print(f"{self.name}, You had {self.balance} rs. left in acc {self.acc} ")


c= input("Enter the name of the bank: ")
a=input("Enter your name: ")
b=int(input("Enter your balance: "))

customer1 = bank(c,a,b,208010458979)
while True:
    choice=int(input("Enter 1 to debit, 2 to credit, 3 to update, 4 to exit: "))
    match choice:
        case 1:
            amount = int(input("Enter amount to debit: "))
            customer1.debit(amount)
        case 2:
            amount = int(input("Enter amount to credit: "))
            customer1.credit(amount)
        case 3:
            customer1.update()
        case 4:
            break
        case _:
            print("Invalid input. Please enter 1 to 4.")