import sys
import openpyxl

wb = openpyxl.load_workbook("banking_database.xlsx")
ws = wb['Sheet 1']

rows = ws.iter_rows(min_row=3,max_row=11,min_col=1,max_col=3)


unidig =[]
nam=[]
bal=[]

for a,b,c in rows:
    unidig.append(a.value)
    nam.append(b.value)
    bal.append(c.value)


x = input("please enter your unidigit = ")

for i in unidig:
    if i == x:
        l = unidig.index(i)
        print("your unidigit is  =",i)
        r = (nam[l])
        h= (bal[l])
    

class Account():
    def __init__(self, owner, balance, ):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amt):
        self.balance = self.balance + deposit_amt
        print(f"added {deposit_amt} to your balance")
        
        
    def withdrawal(self, withdrawal_amt):
        if withdrawal_amt <= self.balance:
            self.balance = self.balance - withdrawal_amt
            print(f"your {withdrawal_amt} is withdrawn successfully")
            
        
        else:
            print("sorry insufficient balance")


print("HEY WELCOME TO SNS BANK!!!!!")

Bank = Account(r,h)
print(f" account holder name is :{Bank.owner}")
print(f"available balance in your account is :{Bank.balance}")


def svs():
    global S
    S = input("what service you want from the bank (deposit,withdrawal,loan service)=")

    if S == "withdrawal":
        y = int(input("please enter your withdrawal amount ="))
        print(Bank.withdrawal(y))
        print(f"your remaining Balance is = {Bank.balance}")
        bal[l] = Bank.balance 
        asking()


    elif S == "deposit":
        z = int(input("please enter your deposit amount ="))
        print(Bank.deposit(z))
        print(f"Your Bank Balnce is = {Bank.balance}")
        bal[l] = Bank.balance 
        asking()

    elif S == "loan service":
        p = int(input("enter the amount of short loan that you want till 5000 = "))
        if p > 5000:
             print("sorry cant provide")
        else:
            print(Bank.deposit(p))
            print("after taking loan your balance is ",Bank.balance)
            bal[l]= Bank.balance
            asking()
    else:
         print("sorry this service is not available please try again ☺️")
    asking()

        
       
    
def asking():
    r = input("Do you want any other services yes or no :")
  
    if r == "yes":
        svs()
        
    else:
        print(' thank you for visiting !!!')
        sys.exit()
    
asking()