'''
this program will be a rock paper scissors game for 2 players~
'''

p1 = input("Player 1, what is your name? ")
p2 = input("Player 2, what is your name? ")

points1 = 0
points2 = 0

play1 = input(p1 + ", please enter 'rock' 'paper' or 'scissors' ")

while (play1 != 'rock' and play1 != 'paper' and play1 != 'scissors'):
    play1 = input(p1 + ", please enter 'rock' 'paper' or 'scissors' ")

play2 = input(p2 + ", please enter 'rock' 'paper' or 'scissors' ")

while (play2 != 'rock' and play2 != 'paper' and play2 != 'scissors'):
    play2 = input(p1 + ", please enter 'rock' 'paper' or 'scissors' ")

keep_playing = True
winner = ""

while(keep_playing):
    if play1 == play2:
        winner = 'tie'
    elif play1 == 'rock':
        if play2 == 'scissors':
            winner = p1
        else:
            winner = p2
    elif play1 == 'paper':
        if play2 == 'scissors':
            winner = p2
        else:
            winner = p1
    else:
        if play2 == 'paper':
            winner = p1
        else:
            winner = p2

    if winner == 'tie':
        n = input("The game was a tie! Do you want to play again? Y/N: ")
        if n == 'N':
            keep_playing = False
        else:
            play1 = input(p1 + ", please enter 'rock' 'paper' or 'scissors' ")
            play2 = input(p2 + ", please enter 'rock' 'paper' or 'scissors' ")
    else:
        if winner == p1:
            points1 += 1
        else:
            points2 += 1

        n = input("Congratulations " + winner + " won this round! Play again? Y/N: ")

        if n == 'N':
            keep_playing = False
        elif n == 'Y':
            play1 = input(p1 + ", please enter 'rock' 'paper' or 'scissors' ")
            play2 = input(p2 + ", please enter 'rock' 'paper' or 'scissors' ")
    
print("Thank you for playing, here are the final scores:")
print(p1 + ":" , points1)
print(p2 + ":" , points2)

if points1 > points2:
    print("Good job", p1, "you won.")
elif points2 > points1:
    print("Good job", p2, "you won.")
else:
    print("IT WAS A TIE GUYS")
  
