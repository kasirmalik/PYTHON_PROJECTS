import random


letters = ['a', 'b','c ','d','e','f','g','h','h','i','j','k','l']
symbol = ['!','@','#','$','%','^','(']
numbers =['1','2','3','4','5','6','7','8','4']

print("Welcome to password generator")
nr_letters =int(input("How many letters would u like in password\n"))
nr_symbols =int(input("How many letters would u like in password\n"))
nr_numbers =int(input("How many letters would u like in password\n"))

# password =""
# for char in range(0,nr_letters):
#     password += random.choice(letters)
  
# for char in range(0,nr_symbols):
#     password += random.choice(symbol)
  
# for char in range(0,nr_numbers):
#     password += random.choice(numbers)
# print(password) 
#            HARD LEVEL   
  
password_list =[]
for char in range(0,nr_letters):
   password_list += random.choice(letters)
  
for char in range(0,nr_symbols):
   password_list += random.choice(symbol)
  
for char in range(0,nr_numbers):
   password_list += random.choice(numbers)
print(password_list)  
random.shuffle(password_list)
print(password_list)  
password = ""  
for char in password_list:
   password += char
print(password)   