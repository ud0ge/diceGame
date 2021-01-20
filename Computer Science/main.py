# [[
#
# Tom
#
# OCR Task 2 Dice Game
#
# STARTED 19/1/21
# ENDED 20/1/21
#
# ]]


import random
import time
from datetime import datetime

i = 1
rounds = 5

player1Points = 0
player2Points = 0

player1End = 0
player2End = 0

WinningUser = ""

loggedIn = False

while loggedIn == False:
    password = input("Please enter the password to continue!\n")
    if password == "csproject":
        loggedIn = True
        print("Hello and welcome to my two player dice game. The information follows below:\n\n• The points rolled on each player’s dice are added to their score.\n• If the total is an even number, an additional 10 points are added to their score.\n• If the total is an odd number, 5 points are subtracted from their score.")
        time.sleep(4)
        response = input("Do you understand?\n")
        if response.lower() == "no":
            print("I will give you more time to read them over.")
            time.sleep(5)
    else:
        print("Incorrect password, please try again.")


# ROLLING THE DICE

def roll():

    points = 0

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    dieResult = die1 + die2

    if dieResult % 2 == 0:
        points += 10
    else:
        if points - 5 < 0:
            points = points
        else:
            points -= 5

    if die1 == die2:
        die3 = random.randint(1, 6)
        points = points + die3

    return(points)

# ROUND BASED

for i in range(1, rounds):
    player1Points += roll()
    print(f"1️⃣   PLAYER1 now has {player1Points} points!\n")
    time.sleep(1)
    player2Points += roll()
    print(f"2️⃣   PLAYER2 now has {player2Points} points!\n")
    time.sleep(1)

# TIE BREAKS

if player2Points == player1Points:
    while player1End == player2End:
        print("TIEBREAKER")
        player1End = random.randint(1, 6)
        player2End = random.randint(1, 6)
    if player1End > player2Points:
        player2Points = 0
    elif player2Points > player1End:
        player1Points = 0

# WINNER

if player1Points > player2Points:
    WinningPoints = player1Points
    WinningUser = "Player 1"

elif player2Points > player1Points:
    WinningPoints = player2Points
    WinningUser = "Player 2"

print(f"🥳 Congratulations {WinningUser} you have won the two player dice game!\nPlease wait while I save this games data!\n")

# SAVING DATA

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

dataFile = open('Data.txt', 'a')
dataFile.write(f"Winner: {WinningUser}\nWinning Points: {WinningPoints}\nTime: {current_time}\n\n")
dataFile.close()
print("Your data has been successfully saved! Thank you for playing! ✔️")

time.sleep(4)