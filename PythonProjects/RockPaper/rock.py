import random
user_choice = int(input("What do u want to choose? type 0 for Rock,1 for Paper or 2 for scissors "))
computer_choice = random.randint(0, 2)
print(f"computer choose {computer_choice}")
if user_choice >= 3 and user_choice < 0:
    print("you choose wrong keyword")      
elif user_choice == 0 and computer_choice ==2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print(" you loose!")    
elif computer_choice > user_choice:
    print("you loose")  
elif user_choice > computer_choice:
    print("you loose")  
elif computer_choice == user_choice:
    print("it's a draw")    
