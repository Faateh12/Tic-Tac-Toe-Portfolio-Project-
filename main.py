choices = ["X", "O"]
choice = input("Choose 'x' or 'o: ").upper()

if choice == "X":
    player1_position = f"|  {choices[0]}  |"
    player2_position = f"|  {choices[1]}  |"
    player2_letter = "O"
elif choice == "O":
    player1_position = f"|  {choices[1]}  |"
    player2_position = f"|  {choices[0]}  |"
    player2_letter = "X"
board = [["|     |" for i in range(3)] for j in range(3)]

# board[p2_x][p2_x] = player2_position
p2_positions = []
p1_pos = []
p2_pos = []
turn = 0

while True:
    if choice == "X" or choice == "O":
        player = None
        player1 = None
        player2 = None
        for i in board:
            print(" ".join(i))
            print("_______________________")
        turn += 1
        if turn % 2 != 0:
            print("Player 1 its your turn")
            player = player1
            if player == player1:
                player = "Player-1"
                position = input(f"{player} ('{choice}') choose a position from 1-9: ")
                if 0 < int(position) <= len(board) * 3:
                    if position == "1":
                        p1_x = 0
                        p1_y = 0
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "2":
                        p1_x = 0
                        p1_y = 1
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "3":
                        p1_x = 0
                        p1_y = 2
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "4":
                        p1_x = 1
                        p1_y = 0
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "5":
                        p1_x = 1
                        p1_y = 1
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "6":
                        p1_x = 1
                        p1_y = 2
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "7":
                        p1_x = 2
                        p1_y = 0
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "8":
                        p1_x = 2
                        p1_y = 1
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    elif position == "9":
                        p1_x = 2
                        p1_y = 2
                        board[p1_x][p1_y] = player1_position
                        board_pos = {player: (p1_x, p1_y)}
                        p2_positions.append(board_pos)
                    else:
                        print("Invalid Input")
                else:
                    turn -= 1
                    print("Invalid Input. Choose a number from 1-9")
        elif turn % 2 == 0:
            print("Player 2 its your turn")
            player = player2
            if player == player2:
                player = "Player-2"
                position = input(f"{player} ('{player2_letter}') choose a position from 1-9: ")
                if 0 < int(position) <= len(board) * 3:
                    if position == "1":
                        p2_x = 0
                        p2_y = 0
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "2":
                        p2_x = 0
                        p2_y = 1
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "3":
                        p2_x = 0
                        p2_y = 2
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "4":
                        p2_x = 1
                        p2_y = 0
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "5":
                        p2_x = 1
                        p2_y = 1
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "6":
                        p2_x = 1
                        p2_y = 2
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "7":
                        p2_x = 2
                        p2_y = 0
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "8":
                        p2_x = 2
                        p2_y = 1
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    elif position == "9":
                        p2_x = 2
                        p2_y = 2
                        board[p2_x][p2_y] = player2_position
                        board_pos = {player: (p2_x, p2_y)}
                        p2_positions.append(board_pos)
                    else:
                        print("Invalid Input")
                else:
                    turn -= 1
                    print("Invalid Input. Choose a number from 1-9")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
        break
    winner = False
    for a in p2_positions:
        for k, v in a.items():
            if k == "Player-1":
                if v not in p1_pos:
                    p1_pos.append(v)
                    # horizontal top win
                    if len(p1_pos) >= 3:
                        if (0, 0) in p1_pos and (0, 1) in p1_pos and (0, 2) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # horizontal bottom
                        elif (2, 0) in p1_pos and (2, 1) in p1_pos and (2, 2) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # horizontal middle
                        elif (1, 0) in p1_pos and (1, 1) in p1_pos and (1, 2) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical left
                        elif (0, 0) in p1_pos and (1, 0) in p1_pos and (2, 0) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical right
                        elif (0, 2) in p1_pos and (1, 2) in p1_pos and (2, 2) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical middle
                        elif (0, 1) in p1_pos and (1, 1) in p1_pos and (2, 1) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # diagonal left corner
                        elif (0, 0) in p1_pos and (1, 1) in p1_pos and (2, 2) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # diagonal right corner
                        elif (0, 2) in p1_pos and (1, 1) in p1_pos and (2, 0) in p1_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
            elif k == "Player-2":
                if v not in p2_pos:
                    p2_pos.append(v)
                    # horizontal top win
                    if len(p2_pos) >= 3:
                        if (0, 0) in p2_pos and (0, 1) in p2_pos and (0, 2) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # horizontal bottom
                        elif (2, 0) in p2_pos and (2, 1) in p2_pos and (2, 2) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # horizontal middle
                        elif (1, 0) in p2_pos and (1, 1) in p2_pos and (1, 2) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical left
                        elif (0, 0) in p2_pos and (1, 0) in p2_pos and (2, 0) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical right
                        elif (0, 2) in p2_pos and (1, 2) in p2_pos and (2, 2) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # vertical middle
                        elif (0, 1) in p2_pos and (1, 1) in p2_pos and (2, 1) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # diagonal left corner
                        elif (0, 0) in p2_pos and (1, 1) in p2_pos and (2, 2) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
                        # diagonal right corner
                        elif (0, 2) in p2_pos and (1, 1) in p2_pos and (2, 0) in p2_pos:
                            winner = True
                            for i in board:
                                print(" ".join(i))
                                print("_______________________")
                            print(f"{k} has won")
    if winner:
        print(p1_pos)
        break
    elif not winner and len(p2_positions) == 9:
        print("Draw")
        break
