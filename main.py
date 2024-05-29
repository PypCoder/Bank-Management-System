import pandas as pd
from datetime import datetime


class Admin:
    def get_admin_data(self):
        data = {
            "name": input("Enter Name: "),
            "age": int(input("Enter Age: ")),
            "gender": input("Enter Your Gender: "),
            "contact": input("Enter Your Contact: "),
            "email": input("Enter Email: "),
            "account_no": int(input("Enter Account No: ")),
            "pin": int(input("Enter Your Pin: ")),
            "balance": int(input("Enter Balance: ")),
        }
        return data
    def make_admin(self,user_data,path):
        df=pd.DataFrame(user_data,index=[0])
        df.to_csv(path,mode="a",header=False,index=False)

class User(Admin):
    def __init__(self,name="",age=0,gender="N/A",contact="",email="",account_no=0,pin=0,balance=0):
        self.name=name
        self.age=age
        self.gender=gender
        self.contact=contact
        self.email=email
        self.account_no=account_no
        self.pin=pin
        self.balance=balance
        if name:
            pass
        else:
            try:
                data= {
                    "name":self.name,
                    "age":self.age,
                    "gender":self.gender,
                    "contact":self.contact,
                    "email":self.email,
                    "account_no":self.account_no,
                    "pin":self.pin,
                    "balance":self.balance,
                }
                self.make_admin(data,"user_data.csv")
            except Exception as e:
                print(f"Error Occured: {e}")
    def display_user_data(self):
        print(f"User Details:\nName:{self.name}\nAge:{self.age}\nGender:{self.gender}\nContact:{self.contact}\nEmail:{self.email}\nAccount No:{self.account_no}\nPin:{self.pin}\nBalance:{self.balance}\n")

class Bank(User):
    def __init__(self,name="",age=0,gender="N/A",contact="",email="",account_no=0,pin=0,balance=0):
        super().__init__(name,age,gender,contact,email,account_no,pin,balance)
    def check_user(self,pin,email):
        self.df=pd.DataFrame(pd.read_csv("user_data.csv"))
        row=list(self.df.get("email",None))
        if email in row:
            if pin == self.df.loc[row.index(email),"pin"]:
                return (True,"",row[0])
            else:
                return (False,"Incorrect Pin","")
        else:
            return (False,"Incorrect Email","")
    def remove_duplicate_acc(self):
        self.df=self.df.drop_duplicates()
        self.df.to_csv("user_data.csv",index=False)
    def display_bal(self):
        print(f"Current Balance:{self.balance}")
    def deposit(self,email,amount=0):
        self.balance+=amount
        self.df[self.df["email"]==email]["balance"]=self.balance
        print(f"Action Successful!\nNew Balance:{self.balance}\n")
    def withdrawal(self,email,amount=0):
        if self.balance>=amount:
            self.balance-=amount
            self.df[self.df["email"] == email]["balance"] = self.balance
            print(f"Action Successful!\nNew Balance:{self.balance}\n")
        else:
            print("Not Enough Balance!")
    def transactions(self,email,amount):
        user_input=int(input("Enter The Desired Action:\nDeposit / Withdraw(1/2): "))
        transaction_data={
            "email":email,
            "amount":amount,
            "action":"",
            "date":datetime.now().date().strftime("%d-%m-%y"),
            "time":datetime.now().time(),
        }
        df=pd.DataFrame(transaction_data,index=[0])
        if user_input==1:
            self.deposit(email,amount)
            df["action"]="Deposited"
            self.make_admin(df,"transaction_data.csv")
        elif user_input==2:
            self.withdrawal(email,amount)
            df["action"]="Withdrawn"
            self.make_admin(df,"transaction_data.csv")
        else:
            print("Invalid Input")
def dashboard():
    bank = Bank("Asad Sagheer",19,"Male","03224415174","asadsagheer243@gmail.com",3224415174,786786,0)
    admin =  Admin()
    new_user=int(input("Sign in or Sign up(1/2): "))
    val, msg, name =False,"No user","N/A"
    if new_user==1:
        email = input("Enter Email: ")
        pin = int(input("Enter Pin: "))
        val, msg ,name = bank.check_user(email=email, pin=pin)
    elif new_user==2:
        try:
            data=admin.get_admin_data()
            admin.make_admin(data,"user_data.csv")
            print(f"Operation Successfull!Welcome aboard {data["name"]}")
            val=True
        except Exception as  e:
            print(f"Error:{e}")
    while True:
        if val:
            if new_user==1:
                print(f"Welcome Back! {name}")
            elif new_user==2:
                print("Welcome to The Bank!")
            while True:
                user_input=int(input("Enter Service You want to Avail:\n1.Open Account\n2.Show User Details\n3.Make a Transaction\n4.Check Balance\n5.Log out\nEnter: "))
                if user_input==1:
                    name,age,gender,contact,email2,account_no,pin2,balance=input("Enter Name: "),int(input("Enter Age: ")),input("Enter Your Gender: "),input("Enter Your Contact: "),input("Enter Email: "),int(input("Enter Account No: ")),int(input("Enter Your Pin: ")),int(input("Enter Balance: "))
                    bank2=Bank(name,age,gender,contact,email2,account_no,pin2,balance)
                    val2,msg2=bank2.check_user(email=email2,pin=pin2)
                    if val2:
                        bank2.remove_duplicate_acc()
                        print("User Already exists!")
                    else:
                        print("Operation Sign Up Successful!")
                elif user_input==2:
                    bank.display_user_data()
                elif user_input==3:
                    bank.transactions(email=email,amount=int(input("Enter Amount: ")))
                elif user_input==4:
                    bank.display_bal()
                elif user_input==5:
                    print("Thank you for your time!")
                    exit(0)
                else:
                    print("INVALID INPUT!")
        else:
            print(msg)
            email = input("Enter Email: ")
            pin = int(input("Enter Pin: "))



if __name__=="__main__":
    dashboard()