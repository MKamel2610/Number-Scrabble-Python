#<<<<<<< Welcome and game rules >>>>>>>
print("Welcome to NUMBER SCRABBLE")
print("Players take turns to pick a number from 1 to 9 and whoever picks three numbers that add up to 15 first wins.")
print("Once a number is picked, it cannot be picked again.")
print()

#<<<<<<< initial game status >>>>>>>
Main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player_1_list = []
player_2_list = []
game_over = False

print(Main_list)
print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list)


while not game_over:   #Turns' iteration 

#<<<<<<< 1st player's play >>>>>>>
    while not game_over:
        player_1_input = input("Player 1's turn. Enter a number: ")
        try:
            number1 = int(player_1_input)
            if number1 in Main_list:
                player_1_list.append(number1)
                Main_list.remove(number1)       #removing the picked number from the main list
                print("\nMain List:", Main_list)
                print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list)
                break
            else:
                print()
                print("Invalid choice. Choose another number\n")
                print("Main List:", Main_list)
                print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list)
        except ValueError:              #entering a non integer value
            print()
            print("Invalid choice. Enter a number\n")
            print("Main List:", Main_list)
            print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list)

#<<<<<<< checking if the 1st player wins >>>>>>>
    n = len(player_1_list)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum1 = player_1_list[i] + player_1_list[j] + player_1_list[k]
                if sum1 == 15:
                    print("Player 1 wins as",player_1_list[i], "+" ,player_1_list[j], "+" ,player_1_list[k],"= 15")
                    game_over = True
                    break

#<<<<<<< checking if the game is a draw >>>>>>>
    if not game_over and not Main_list:
        print("The game is a draw!")
        game_over = True

#<<<<<<< 2nd player's play >>>>>>>
    while not game_over:
        player_2_input = input("Player 2's turn. Enter a number: ")
        try:
            number2 = int(player_2_input)
            if number2 in Main_list:
                player_2_list.append(number2)
                Main_list.remove(number2)
                print("\nMain List:", Main_list)
                print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list, "\n")
                break
            else:
                print()
                print("Invalid choice. Choose another number\n")
                print("Main List:", Main_list)
                print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list, "\n")
        except ValueError:              #entering a non integer value
            print()
            print("Invalid choice. Enter a number\n")
            print("Main List:", Main_list)
            print("Player 1:", player_1_list, " " * 30, "Player 2:", player_2_list, "\n")

#<<<<<<< checking if the 2nd player wins >>>>>>>
    n = len(player_2_list)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                sum2 = player_2_list[i] + player_2_list[j] + player_2_list[k]
                if sum2 == 15:
                    print("Player 2 wins as",player_2_list[i], "+" ,player_2_list[j], "+" ,player_2_list[k],"= 15")
                    game_over = True
                    break
