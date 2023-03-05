from random import randint

arr = [1,2,3,4,5,6]

def casino():
     user_P = 500
     play = True
     pc_choice = randint(1,50)
     while play:
              
          user_c = int(input(f"chose number(1-50){user_P}:"))
          if user_P <= 0:
               print(f"FUCK LUSER{user_P},{pc_choice}")
               play = False
          elif user_c > pc_choice:
               user_P = user_P - 20
               print(f"lower{user_P},{pc_choice}")
          elif user_c < pc_choice:
               user_P = user_P - 20
               print(f"HIGHER{user_P},{pc_choice}")
          elif user_c == pc_choice:
               user_P = user_P + 20
               print(f"GET Money!!,{pc_choice},user_p = {user_P} ")
               pc_choice = randint(1,50)
               #pc_choice가 같은 번호가 되어지지 않게 끝나고 나서 한번더 선언


casino()    

     
     

     