# class amt (Exception):
#     pass

# def bank():
#     if amount<balance:
#         raise amt ("withdraw unsuccessfull!!")
#     else:
#         print("withdraw successful")
        

# try:
#     name=input("Enter the name : ")
#     accno=int(input("Enter the accno : "))
#     amount=int(input("Enter the amount : "))
#     balance=int(input("Enter the balance : "))
#     withdraw=balance-amount
#     print("Yours withdraw amount : ",withdraw)
# except amt as e:
#     print(e)

# class withdraw(Exception):
#     pass

# def bank(balance,amount):
#     if balance < amount:
#         raise withdraw("insuffient balance!!")
#     else:
#         totalbalace = balance - amount
#         print("your Current Balance is:",totalbalace)         

# name= input("Enter your name:")
# accno=int(input("Enter your account number:"))
# amount = int(input("Enter the amount to withdraw:"))
# balance = int(input("Enter the balance amount in your bank:"))
# try:
#     bank(balance,amount)
# except withdraw as e:
#     print(e)

class Error(Exception):
    pass

def check_email(email_address):
    if "@" not in email_address:
        raise Error("Invalid email address!")
    else:
        print("Valid email address")

email = input("Enter the email: ")

try:
    check_email(email)  
except Error as e:
    print("exception",e)

