import random
import time

def displayIntro():
    print 'You are in a land full of dragons.'
    print 'in front of you, you see two caves.'
    print 'In one cave, the dragon is friendly and will share his treasure with you.'
    print 'The other dragon is greedy and hungry, and will eat you alive.'
    print

def chooseCave():
    while (True):
        print 'Choose a cave (1 or 2):'
        cave = raw_input()
        if (cave == '1' or cave == '2'):
            return cave
        print 'Please enter a valid number!'

def badEnding():
    print 'NOM!'

def goodEnding():
    print 'Yay!'

def checkCave(chosenCaveStr):
    time.sleep(1)
    print 'You approach the cave...'
    time.sleep(1)
    print 'It is dark and spooky...'
    time.sleep(1)
    print 'A large dragon jumps out in front of you!'
    time.sleep(1)
    print 'He opens his jaws & ...'
    dragonCaveStr = str(random.randint(1,2))
    time.sleep(3)
    if (dragonCaveStr == chosenCaveStr):
        badEnding()
    else:
        goodEnding()

playAgain = 'Yes'
while playAgain == 'Yes' or playAgain == 'Y':

    displayIntro()
    checkCave(chooseCave())

    print 'Do you want to play again? (Yes or No)'
    playAgain = raw_input()
    if (playAgain != 'Yes' and playAgain != 'Y' and playAgain != 'y'):
        print 'Ending Game!'
        print        
        break