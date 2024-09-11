print("Welcome to treasure island")
print("Your mission is to find the treasure")
choice1 =input('you are at a crossword, where you want to go? type "Left" orr "Right"').lower()
if choice1 == "left":
    choice2=input('you have come to a lake. there is a island in the middle of lake.type "wait" to wait forboat type "swim" for swin across').lower()
    if choice2 =="wait":
        choice3 == input('You arrive at the island unharmed.there is a house with 3 doors. one "red","one yellow and on blue"."which color do you choose"')
        if choice3  =="red":
            print("it is room of fire game over")
        elif choice3 =="yellow":
            print("you found a treasure you win")
        elif choice3 == "blue":
            print("you entered room of beasts. game over")
        else:   
            print("you choose wrong door")   
    else:
        print("you are attacked by beasts")          
else:
    print("you fell in hole")