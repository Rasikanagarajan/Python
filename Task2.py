# nested if

Name = input("Enter your Name :")
Password=int(input("ENter your pw :"))
name="Rasika"
pw=123

if name==Name:
    if pw==Password:
        print("matched")
    else:
        print("doesnt match")

# Electricity bill

unit=int(input("Enter your Electricity Bill :"))
if unit<=100:
    print("your unit is limit so...No need to pay")
elif unit>100:
    print("$",unit*2)
elif unit>500:
    print("$",unit*3)
elif unit>1000:
    print("$",unit*5)
else:
    print("Invalid")

# Even Numbers

for i in range(0,500,2):
    print(i,end=" ")


animals = ("dog","cat","cow","elephant","tiger","lion","cheetah")
for i in animals:
    if i=="dog":
        print("Match found",i)
        continue
    else:
        print("Match not found",i)
        
# Prime numbers

num = int(input("Enter the number: "))
for i in range(2,100):
    if num%2!=0:
        print(num) 

