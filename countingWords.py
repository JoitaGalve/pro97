
>>> import random
>>> print("Number guessing number")
Number guessing number
>>> number = random.randint(1, 9)
>>>
>>> chances = 0
>>> print("Guess a number (between 1 and 9):")
Guess a number (between 1 and 9):
>>>
>>>
>>> while chances < 5:
...
...      guess = int(input("Enter your guess: "))
...
...
>>> print(guess)
9
>>>
IndentationError: unexpected indent
>>> if guess == number:
...    print("Congratulation You Won!!!")
...    break
...
  
>>> elif guess < number:
...      print("Your guess was too low:Guess a higher number than", guess)

>>>else:
...   print("Your guess was too high:Guess a lower number than", guess)

>>>chances == 1

>>>if chances < 5:
...   print("YOU LOSE!!! The number is", number)