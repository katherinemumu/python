'''
this is the cows and bulls game
cows: the number is right and in the right place
bull: the number is there but in the wrong place
'''
import random

if __name__ == "__main__":
    num = list(str(random.randint(1000,9999)))
    # print(num)
    correct = False
    
    x = list(input("Enter your guess: "))

    while(not correct):
        cows = 0
        bulls = 0
        for i in range(len(x)):
            if x[i] == num[i]:
                cows += 1
            elif num[i] in x:
                bulls += 1
        if cows == 4:
            correct = True
            print("Congratulations, you won!")
        else:
            print("Cows:", cows)
            print("Bulls:", bulls)
            x = list(input("Enter your guess: "))    
        
