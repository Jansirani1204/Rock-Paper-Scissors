import random

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

#Write your code below this line 👇
print("Welcome to rock paper sissor game!!")
user_choice = int(input("What do you wanna choose? Type 0 for rock, 1 for paper, or 2 for scissors.\n"))
#user side
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

#computer side
computer_choice = random.randint(0,2)
print("Computer chose:")
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)

#game logic
if user_choice == 0:
   if computer_choice == 1:
         print("you lose")
   elif computer_choice == 2:
         print("you win")
   else:
       print("Draw")
if user_choice == 1:
   if computer_choice == 2:
         print("you lose")
   elif computer_choice == 0:
         print("you win")
   else:
       print("Draw")
if user_choice == 2:
   if computer_choice == 0:
         print("you lose")
   elif computer_choice == 1:
         print("you win")
   else:
       print("Draw")