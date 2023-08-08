# Ask user for number of pencils
import random


def winning_move(pencils):
    if pencils % 4 == 0 and pencils % 2 == 0:
        return 3
    elif pencils % 2 == 0:
        return 1
    elif pencils == 1:
        return 1
    else:
        return 2


total_pencils = input("How many pencils would you like to use: ")
while True:
    if total_pencils.isnumeric():
        if total_pencils == '0':
            print("The number of pencils should be positive")
            total_pencils = input()
            continue
        else:
            break
    else:
        print("The number of pencils should be numeric")
        total_pencils = input()
        continue

total_pencils = int(total_pencils)
# Ask to input first player name
first_player = input("Who will be the first (John, Jack): ")

while True:
    if first_player == 'John' or first_player == 'Jack':
        break
    else:
        first_player = input("Choose between 'John' and 'Jack' ")

print(total_pencils * '|')

player_list = ['John', 'Jack']  # Make a list of 2 players
player_index = player_list.index(first_player)  # Obtain the index

while total_pencils > 0:
    print(f"{player_list[player_index]}'s turn:")

    if player_index == 1:
        remove_pencils = winning_move(total_pencils)
        print(remove_pencils)
    else:

        while True:
            remove_pencils = input()
            if remove_pencils.isdigit():
                if int(remove_pencils) in [1, 2, 3]:
                    if total_pencils >= int(remove_pencils):
                        break
                    else:
                        print("Too many pencils were taken")
                        continue
                else:
                    print("Possible values: '1', '2' or '3'")
                    continue
            else:
                print("Possible values: '1', '2' or '3'")
                continue
                # remove_pencils = input()

    remove_pencils = int(remove_pencils)
    total_pencils -= remove_pencils

    print(total_pencils * '|')

    player_index = 1 - player_index  # Change index value to switch players

# Reverse index change on last iteration to indicate winner
print(f"{player_list[player_index]} won!", end="")
exit()
