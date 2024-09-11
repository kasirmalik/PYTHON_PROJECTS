# height = 20
# if height >= 20:
#     print("you can ride")
# else:
#     print("sorry can't ride")

# even number

# evennum = int(input("Please enter no: "))
# if evennum % 2 == 0:
#     print("even no")
# else:
#     print("odd number")    
# even= 1
# if even == 0:
#     print("even")
#     eventwo = 3
#     if eventwo == 2:
#         print("two")
#     else:
#         print("three")

#         # comment: 
#     # end if
# else:
#     print("odd")  
height = int(input("Please enter your height : ")) 
bill = 0
if height >= 180:
    print("you can rid ethe the roller coster")
    age =int(input("Please enter your age: "))
    if age <= 12:
        bill = 5
        print("child ticket are 5$")
    elif age<= 18:
        bill=7
        print("youth ticket are 7$") 
    else:
        bill =12
        print("adult ticket are 12$")
    wants_photo = input("do you want to take photo? type y for yes and n for no.") 
    if wants_photo =="y":
        bill += 3
    print(f"your final bill is {bill}")         
else:
    print("sorry have to be taller to ride roller coster")         