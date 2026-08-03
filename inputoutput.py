# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# print("sum of two number",a+b)
# print("substrect the two number",a-b)

# print( "devide two number",a/b)
# print( "multiplication of two numbers", a*b)
# 8

# input("enter your name:")
# input("enter your address:")
# input("enter your introduction:")
# print(input)

# age = int(input("enter your age:"))
# if age>=18:
#     print("you are eligible for voting")
# else:
#     print("you are not eligible:")

# a = int(input("enter the first number:"))
# b = int(input("enter the second number:"))
# c = int(input("enter the third number:"))
  
# if a>b and a>c:
#     print("a is greater:")
# elif b>a and b>c:
#     print("b is greater:")
# else:
#     print("c is greater:")          


# year = int(input("enter year:"))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("LEAP YEAR")
# else:
#     print("it is not leap year")    


# username = input("enter your user name:")
# password = input("set your password:")

# if username == "admin":
#     if password == "1234":
#         print("login successfull")
#     else:
#         print("wrong password:")
# else:
#     print("try again")            

# username = input("enter your username:")
# password = input("set your password:")

# if username == "mohdzaid":
#     if password == "8206":
#         print("login succesfully")
#     else:
#         print("wrong password")
# else:
#     print("try again")            

math = int(input("enter your marks in maths:"))

science = int(input(" enter your marks in science:"))

history = int(input("enter your marks in history"))

total = math+science+history
percentage = total/3

if math<33 or science<33 or history<33:
    print("fail")
elif percentage >=90:
    print("GRADE A")
elif percentage >=80:
    print("GRADE B")
elif percentage >=70:
    print("GRADE C") 
elif percentage >=60:
    print("GRADE D") 
else:
    print("JUST PASS")                  