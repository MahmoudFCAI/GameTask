# File: CS112_A1_T2_game 2_20230374.py.
# Purpose: Players should alternate picking numbers from 1 to 9, the player that collect 3 numbers that add equal 15 win
# Author: Mahmoud Ali Anwar Mohamed
# ID: 20230374

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Store numbers chosen by the player one
array_one = []


# Store numbers chosen by the player two
array_two = []


# Remove numbers selected form both players
def RemoveNumber(numbers_list, number):
    numbers_list = [num for num in numbers_list if num != number]
    return numbers_list


# Check are there any numbers whose sum  is equal 15 or not
def check_sum(array):
    if len(array) < 3:
        return False

    for i in range(len(array) - 2):
        for j in range(i + 1, len(array) - 1):
            for k in range(j + 1, len(array)):
                if array[i] + array[j] + array[k] == 15:
                    return True
    return False


# Check is the array become  empty or not
def check_empty(numbers):
    if not numbers:
        return True
    return False


# Displays the latest update for each player
def print_arrays(array_one, array_two):
    print("_____________________________________________\n")
    print(f"numbers of player one become: {array_one}")
    print(f"numbers of player two become: {array_two}")


# Explanation the game
print('**  We will now play a game of number scrabble ** \n ')
print('''*** played with the list of numbers between 1 and 9 Each player takes a number Once a number has been taked,it cannot be taked again.
    If a player taked three numbers it sum equal 15, that player wins the game, or if all the numbers are used and no player gets exactly 15, the game is a draw. *** ''')

# Go down line
print('\n')


while (True):

    # Player one chooses the numbers
    num_one = int(
        input(f"Player one. Please select number from  this list {numbers}: "))


# Check whether the number entered by the player one  is in the list or not
    while (num_one not in numbers):
        num_one = int(
            input(f"Player one. Please select  a vaild number from this list: {numbers}: "))


#  Add number to array one
    array_one.append(num_one)


#  Remove number from list of numbers
    numbers = RemoveNumber(numbers, num_one)


#  Check does the sum is equal 15 or not
    result = check_sum(array_one)
    if (result == True):
        print_arrays(array_one, array_two)
        print("Player one won.")
        break


# Check does the array  is empty or not
    is_empty = check_empty(numbers)
    if (is_empty == True):
        print_arrays(array_one, array_two)
        print("The game is a draw.")
        break

# Display the list of numbers that the player two chose
    is_empty = check_empty(array_two)
    if (is_empty == False):
        print(f"numbers of player two  become: {array_two}")


# Player two  chooses the numbers
    num_two = int(
        input(f"Player two. Please select number from list {numbers} : "))


# Check whether the number entered by the player two  is in the list or not
    while (num_two not in numbers):
        num_two = int(
            input(f"Player two. Please select  a vaild number from this list: {numbers} : "))


#  The number was chosen  by player two is added to the array
    array_two.append(num_two)

# Check does the sum is equal 15 or not
    result = check_sum(array_two)
    if (result == True):
        print_arrays(array_one, array_two)
        print("Player two won.")
        break


#  The number was chosen  by player two is remove from numbers
    numbers = RemoveNumber(numbers, num_two)


# Display the list of numbers that the player one chose
    print(f"numbers of player one  become: {array_one}")
