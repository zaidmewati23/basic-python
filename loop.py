
# for i in range(100):
     
#      i = "I LOVE YOU"
#      print(i)

# for i in range(23):
#     i = "TERI MA KI CHOOT BHKLND"
#     print(i)

# f i in range(1,20,2):
#     print(i)

# for i in range(1,11):
#     i = i*10
#     print(i)


# for table in range(1,6):
#     print(f"\n Table of {table}")
#     print("-" * 15)

#     for number in range(1,11):
#         result = table*number
#         print(f"{table} x {number} = {result}")
#         print("\n all tables completed!")

# num = int(input("enter the number:"))
# if num<2:
#     print("not prime")
# else:
#     for i in range(2,num):
#         if num%i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")   

# n = int(input("enter the number:"))  
# if n<2:
#     print("not prime ")
# else:
#     for i in range(2,n):
#         if n%i == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")                 

# n = int(input("enter a number:"))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print("factorial=",fact)   
# #********************************
# n = int(input("enter a number:"))
# fact = 1
# for i in range(1,n+1):
#     fact*= i
# print("factorial..",fact)    


# n = int(input("enter a number:"))
# fact = 1
# for i in range(1,n+1):
#     fact *= i
# print("factorial...",fact)    




# n = int(input("how many terms?"))
# a,b = 0,1
# for i in range(n):
#     print(a, end=" ")
#     a ,b = b ,a+b

# n = int(input("how many terms?"))
# a,b = 0,1
# for i in range(n):
#     print(a, end="   ")
#     a,b = b, a+b    





# n = int(input("how many terms?"))
# a , b = 0 , 1
# for i in range(n):
#     print(a, end="     ")
#     a  ,  b = b , a+b


# n = int(input("enter the number -> "))
# rev = 0

# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n//=10
# print("reverse =",rev)    

# n = int(input("enter the number:"))

# rev = 0
# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n //=10
# print("reverse...",rev)    

# n = int(input("enter the number:"))
# rev = 0
# orignal = n

# while n>0:
#     digit = n%10
    
#     rev = rev*10+digit
#     n  //=10
# if orignal == rev:
#         print("POLINDROM")
# else:
#         print("NOT POLINDROM ")    

# n = int(input("enter number->"))
# rev = 0
# orignal = n

# while n>0:
#     digit = n%10
#     rev = rev*10+digit
#     n //=10
# if orignal == rev:
#     print("POLINDROM") 

# else:
#     print("NOT POLINDROM")       
# n = 5
# for i in range(1,n+1):
#     space = n-i
#     stars = 2*i-1

#     print(" " * space + "*" * stars)

