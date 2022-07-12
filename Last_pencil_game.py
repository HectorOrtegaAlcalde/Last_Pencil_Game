#-------------------------------------------------------------------------------
# Name:        Last Pencil
# Purpose:
#
# Author:      Hector Ortega
#
# Created:     12/07/2022
# Copyright:   (c) Hector 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# The last pencil game consists in achieving that the other player takes the
# last pencil standing on the board. In this game mode the opponent (Irene)
# is a bot programmed to follow the winning strategy.

def bot_turn(num_pencils):
    if num_pencils % 4 == 0:
        pencils_taken = 3
    elif num_pencils % 4 == 3:
        pencils_taken = 2
    elif num_pencils % 4 == 2:
        pencils_taken = 1
    else:
        pencils_taken = 1
    return pencils_taken


while True:
    print("How many pencils would you like to use:")
    while True:
        num_pencils = input()
        if num_pencils.isnumeric() == False:
            print("The number of pencils should be numeric")
            continue
        else:
            num_pencils = int(num_pencils)
            if num_pencils < 0:
                print("The number of pencils should be numeric")
                continue
            elif num_pencils == 0:
                print("The number of pencils should be positive")
                continue
            else:
                break
    print("Who will be first (Hector, Irene)")
    while True:
        first_player = input()
        if (first_player != "Hector") and (first_player != "Irene"):
            print("Choose between 'Hector' and 'Irene'")
            continue
        else:
            break
    if first_player == "Hector":
        second_player = "Irene"
    else:
        second_player = "Hector"
    print(num_pencils*"|")
    possible_values = [1, 2, 3]
    turns = 0
    while num_pencils > 0:
        if turns % 2 == 0:
            print(f"{first_player}'s turn")
        else:
            print(f"{second_player}'s turn")
        if (first_player == "Hector" and turns % 2 == 0) or (second_player == "Hector" and turns % 2 != 0):
            while True:
                n = input()
                if n.isnumeric() == False:
                   print("Possible values: '1', '2' or '3'")
                   continue
                else:
                    n = int(n)
                    if n not in possible_values:
                        print("Possible values: '1', '2' or '3'")
                        continue
                    elif num_pencils - n < 0:
                        print("Too many pencils were taken")
                        continue
                    else:
                        break
        else:
            n = bot_turn(num_pencils)
        if num_pencils - n == 0 and turns % 2 == 0:
            print(f"{second_player} won!")
            break
        elif num_pencils - n == 0 and turns % 2 != 0:
            print(f"{first_player} won!")
            break
        else:
            num_pencils -= n
            print(num_pencils*"|")
            turns += 1
    break



#To play with two players:
"""
while True:
   print("How many pencils would you like to use:")
   while True:
        num_pencils = input()
        if num_pencils.isnumeric() == False:
            print("The number of pencils should be numeric")
            continue
        else:
            num_pencils = int(num_pencils)
            if num_pencils < 0:
                print("The number of pencils should be numeric")
                continue
            elif num_pencils == 0:
                print("The number of pencils should be positive")
                continue
            else:
                break
    print("Who will be first (Hector, Irene)")
    while True:
        first_player = input()
        if (first_player != "Hector") and (first_player != "Irene"):
            print("Choose between 'Hector' and 'Irene'")
            continue
        else:
            break
    if first_player == "Hector":
        second_player = "Irene"
    else:
        second_player = "Hector"
    print(num_pencils*"|")
    possible_values = [1, 2, 3]
    turns = 0
    while num_pencils > 0:
        if turns % 2 == 0:
            print(f"{first_player}'s turn")
        else:
            print(f"{second_player}'s turn")
        while True:
            n = input()
            if n.isnumeric() == False:
               print("Possible values: '1', '2' or '3'")
               continue
            else:
                n = int(n)
                if n not in possible_values:
                    print("Possible values: '1', '2' or '3'")
                    continue
                elif num_pencils - n < 0:
                    print("Too many pencils were taken")
                    continue
                else:
                    break
        if num_pencils - n == 0 and turns % 2 == 0:
            print(f"{second_player} won!")
            break
        elif num_pencils - n == 0 and turns % 2 != 0:
            print(f"{first_player} won!")
            break
        else:
            num_pencils -= n
            print(num_pencils*"|")
            turns += 1
    break
"""
