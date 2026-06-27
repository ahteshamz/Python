import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 60)
    #Fetch the score
    try:
        with open("Practice/hiscore.txt") as f:
            hiscore = f.read()
            if(hiscore!=""):
                hiscore = int(hiscore)
            else:
                hiscore = 0
    except FileNotFoundError:
        hiscore = 0
            
    print(f"Your score: {score}")
    if(score>hiscore):
        #Write this score in the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))
    return score
game()