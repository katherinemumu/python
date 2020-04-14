import random

x = random.randint(1,9)

count = 1
guess = input("Enter a guess: ")    

while (guess == 'exit' or int(guess) != x):
    guess = int(guess)
    if guess > x:
        print("Too High!")
    else:
        print("Too Low!")
    guess = input("Enter a guess: ")
    count += 1

if guess == 'exit':
    print("Thank you for playing:), the correct answer was", x)
else:
    print("Good job! You won! It took you", count, "tries.")
