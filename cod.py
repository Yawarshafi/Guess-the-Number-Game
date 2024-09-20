# @yawarshafi
import random

random_num = random.randint(1, 50)


print("Guess the Number Game!!!")
starter = int(input("Press 7 to start the Game!:"))
if(starter == 7):
    print("Press `Q` at any stage to quit the game!")
    while True:
        guess = (input("Guess the Number(1-50):"))
    
        if(guess == "Q"):
            break

        guessed_num= int(guess)
        if(guessed_num == random_num):
            print("!!!!!!!!!!!!!!Success!!!!!!!!!!!!!!")
            break
        elif(guessed_num > random_num):
            print("Target number is less than that")
        else:
            print("Target number is greater than that.")

    print("Game Over!")

else:
    print("You did not press 7")

# @yawarshafi
