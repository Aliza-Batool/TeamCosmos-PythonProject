import random
num=random.randint(1,50)
print("====THE NUMBER GUESSING GAME====")
print("A number has been generated randomly.")
print("You have 10 tries to guess the number.")
print("The number is between 1-50.")
guess=0
i=0
while guess!=num and i<10:
     i+=1
     guess=int(input("Enter your guess: "))
     if guess>num:
          print("Your guess is too high. Guess lower.")
     elif guess<num:
           print("Your guess is too low. Guess higher.")
if guess==num:
     print("You guessed the correct number!")
if guess!=num and i==10:
     print("Oops!You are out of tries!")