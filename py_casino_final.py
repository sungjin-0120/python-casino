from random import randint
pc_choice = randint(1,50)


user_P = 500
play = True
while play:
     user_c = int(input(f"chose number(1-50){user_P}:"))
     if user_P <= 0:
          print(f"FUCK LUSER{user_P},pc_choice:{pc_choice}")
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
          pc_choice = randint(1, 50)
               
     
     

     