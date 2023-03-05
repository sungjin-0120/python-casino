from random import randint
pc_choice = randint(1,50)
arr = [1,2,3,4,5,6]

def casino():
     user_P = 100
     play = True
     while play:
          user_c = int(input(f"chose number(1-50){user_P}:"))
          if user_P <= 0:
               print(f"FUCK LUSER{user_P}")
               play = False
          elif user_c > pc_choice:
               user_P = user_P - 20
               print(f"lower{user_P}")
          elif user_c < pc_choice:
               user_P = user_P - 20
               print(f"HIGHER{user_P}")
          elif user_c == pc_choice:
               user_P = user_P + 20
               print(f"GET Money!!,{pc_choice},user_p = {user_P} ")
               pc_choice2 = randint(1, 50)
               while play:
                    user_c = int((input(f"chose number(1-50){user_P}:")))
                    if user_P <= 0:
                         print(f"FUCK LUSER{user_P}")
                         play = False
                    elif user_c > pc_choice2:
                         user_P = user_P - 20
                         print(f"lower{user_P}")
                    elif user_c < pc_choice2:
                         user_P = user_P - 20
                         print(f"HIGHER{user_P}")
                    elif user_c == pc_choice2:
                         user_P = user_P + 20
                         print(f"GET Money!!,{pc_choice2},user_p = {user_P}  ")

for ar in arr:
     casino()    

     
     

     