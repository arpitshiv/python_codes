from random import *
test_seed=int(input("enter seed value"))
seed(test_seed)

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
game_images=[rock,paper,scissors]
user_input=int(input("enter 0 for rock,1 for paper,2 for scissor"))
print("your choice"+game_images[user_input])
ai_choice=randint(0,2)
print("computr choice"+game_images[ai_choice])
if (user_input>=3 or user_input<0):
    print("invalid entries")
elif(user_input==ai_choice):
    print("its a draw")
elif(user_input==0 and ai_choice==2):
    print("you won")
elif(user_input==2 and ai_choice==0):
    print("you lose")

elif(user_input<ai_choice):
    print("you lose")
elif(user_input>ai_choice):
    print("you won")
    