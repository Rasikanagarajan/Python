try:
    name=input("Enter a Name : ")
    passwrd=input("Enter a password : ")
    phone=input("Enter a phone : ")
    address=input("enter the address : ")
   
except (ValueError,Exception) as e:
    print("Error",e)
else:
    if len(passwrd) >=8:
        print(passwrd)
    else:
        print("enter a valid password")
    if len(phone) == 10 and phone.isdigit():
        print(phone)
    else:
        print("please enter a valid number !")
    print(name,passwrd,phone,address)
finally:
    print("Executed")

