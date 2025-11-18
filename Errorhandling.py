# import task ModuleNotFoundError
# a=23
# print(A) name error
# name=input('enter name) SyntaxError:
# age=int(input("enter age:"))ValueError
# print(age)
# print(task1.Name)
# a=45
# if a<18:
# print("yes")IndentationError
# try:
#     a=int(input("enter a number:"))
# except (ZeroDivisionError,ValueError) as e:
#     print(e)
# except Exception  as e:
#     print("something worng",e)
# else:
#     print(a)
# finally:
#     print("code executed")

# try:
#     a=input("Enter a nane : ")
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print("wrong",e)
# else:
#     print(a)
# finally:
#     print("Good")
class ageNotValid(Exception):
    pass
def age(n):
    if n<=18:
        raise ageNotValid("age lessthan 18")
    else:
        print("acceess allowed")
try:
    age(3)
except ageNotValid as e:
    print(e)


# age=int(input("enter a number"))
# if age<=18:
#     raise ageNotValid("age lessthan 18")
# else:
#     print("acceess allowed")
# if age>=18:
#     raise ValueError("enter age")
# else:
#     print("acceess allowed")
