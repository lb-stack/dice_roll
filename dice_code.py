import random

min_val = 1
max_val = 6 

roll_again = "yes"

while roll_again == "yes":
    print("Rolling the dices...")
    print("The values are:")
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    roll_again = input("Roll the dices again?")



