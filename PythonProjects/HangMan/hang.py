word_list = ["aardwark","baboon","camel"]

#randomly choose word from word list
import random
lives = 6
choosen_word = random.choice(word_list)
print(choosen_word)

# create a place holder with same number of blanks+
placeholder = ""
word_length = len(choosen_word)
for postion in range(1,6):
    placeholder += "_"
print(placeholder)   

# ask the user to guess the letter
game_over = False
correct_letters = []
while not game_over :
    guess = input("Guess a letter: ").lower()
    print(guess)

    if guess in correct_letters:


    #create a display that puts the guessed letter in right position
       display = ""



# check if the letter the user entered is correct
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter    
        else:
            display += "_"

    print(display)  
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you loose.")

    if "_" not in display:
        game_over = True
        print("You win")

       