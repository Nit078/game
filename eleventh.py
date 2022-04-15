import random
rock = ('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')

paper = ('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    ''')

scissor = ('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

a=int(input("What do you choose 0,1,2 : \n "))
if a==0:
   print(rock)
elif a==1:
   print(paper)
else:
   print(scissor)
c=random.randint(0,2)
print(f"Computer chooses: {c}")
if c==0:
       print(rock)
elif c==1:
   print(paper)
else:
   print(scissor)
c=random.randint(0,2)

    
if a == c:
    print(f"Both players selected {a}. It's a tie!")

elif a == 0 :
    if c == 2 :
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif a == 1 :
    if c == 0 :
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif a == 2 :
    if c == 1 :
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
