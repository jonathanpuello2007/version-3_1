import random


magic_number = random.randint(1,10)
print("Welcome to the Million dollar game, you will have 2 opportunities to try, think carefully")
counter = 1

while counter < 3:
  user_guess = int(input("Guess a number between 1 and 10: "))

  if user_guess == magic_number:
    print("You won!")
    break
  else:
    print("Your guess was incorrect.")

  counter = counter + 1


print("You lose!")
