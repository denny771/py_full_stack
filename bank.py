# Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.
# Give the complete code for the  BankAccount class.




class BankAccount():
    # parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance

    def test(self):
        sum = 3+4
        return sum


class Transactions(BankAccount): 
    #test
    def avg(self):
        av = self.test()/2
        print(av)
    # Deposit method
    def Deposit(self,d):  
        self.balance = self.balance + d
        print("Remaining balance is: ",self.balance)

    # Withdrawal method
    def Withdrawal(self , w):
        
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
            print("Remaining balance is: ",self.balance)


class Fee(Transactions):
    def __init__(self, accountNumber, name, balance):
        super().__init__(accountNumber, name, balance)
    # bankFees method
    def bankFees(self):
        self.balance = (95/100)*self.balance
        print(self.balance)
        
    # display method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance)


# Testing the code :
newAccount = Fee(44684684, "Denny" , 2700)

#dis
newAccount.display()

# Creating Withdrawal Test
newAccount.Withdrawal(300)
# Create deposit test
newAccount.Deposit(200)
# Display account informations
newAccount.display()

newAccount.bankFees()

newAccount.avg()
