import random as rd
import matplotlib.pyplot as plt

def getLosingDoor(host, numOfDoors, playerChoice):
    i = 1
    while (i == host or i == playerChoice):
        i = (i+1) % (numOfDoors)

    return i

def switchDoor(montyDoor, numOfDoors, playerChoice):
    i = 1
    while (i == montyDoor or i == playerChoice):
        i = (i+1) % (numOfDoors)
    return i

def game(switch, numOfTests):
    switchWin = 0
    noSwitchWin = 0
    switchLose = 0
    noSwitchLose = 0
    doors = [0,1,2]
    numOfDoors = len(doors)


    for _ in range(numOfTests):
        car = rd.randint(0, numOfDoors-1)
        host = car

        playerChoice = rd.randint(0, numOfDoors-1) 
        oriChoice = playerChoice
        montyDoor = getLosingDoor(host, numOfDoors, playerChoice)
        if switch == True:
            playerChoice = switchDoor(montyDoor, numOfDoors, playerChoice)

        if playerChoice == host and switch == False:
            # No Switch Win
            print('Player Wins (No switch) - The player chose door: ', playerChoice+1,' Original choice: ', oriChoice+1,', Door with prize:', car+1, ', Shown Door: ',montyDoor+1)
            noSwitchWin += 1
        elif playerChoice == host and switch == True:
            # Switch Win
            print('Player Wins (switch) - The player chose door: ', playerChoice+1,' Original choice: ', oriChoice+1, ', Door with prize:', car+1, ', Shown Door: ',montyDoor+1)
            switchWin += 1
        elif playerChoice != host and switch == False:
            # No Switch Lose
            print('Player Lost (No switch) - The player chose door: ', playerChoice+1,' Original choice: ', oriChoice+1, ', Door with prize:', car+1, ', Shown Door: ',montyDoor+1)
            noSwitchLose += 1
        elif playerChoice != host and switch == True:
            # Switch Lose
            print('Player Lost (switch) - The player chose door: ', playerChoice+1,' Original choice: ', oriChoice+1, ', Door with prize:', car+1, ', Shown Door: ',montyDoor+1)
            switchLose += 1
        else:
            print('Error occurred.')

    return noSwitchWin, switchWin, noSwitchLose, switchLose, numOfTests

choice = input("Switch or Don't Switch? (Input Y for Switch and N for No Switch) ").upper()
loop = int(input("Number of simulation: "))

if choice == "Y":
    count = game(True, loop)
    print('Win Percentage after Switching: ', count[1]/ count[4])
    print('Lose Percentage after Switching: ', count[3]/ count[4])
elif choice == "N":
    count = game(False, loop)
    print('Win Percentage without Switching: ', count[0]/ count[4])
    print('Lose Percentage without Switching: ', count[2]/ count[4])
else:
    print("You need to input either 'Y' or 'N'.")
