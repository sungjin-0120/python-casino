from random import randint
pc_choice = randint(1,50)

play = True
while play:
    user_choice = int(input("choose your number:"))
    if user_choice==pc_choice:
        print(f"you win {pc_choice}")
        play = False
    elif user_choice<pc_choice:
        print("higher")
    elif user_choice >pc_choice:
        print("lower")