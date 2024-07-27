def printBoard(board):
    for row in board:
        print("|".join(row))
        print("-" * 7)

def checkWinner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0][0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
        
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]   
    if board[2][0] == board[1][1] == board[0][2] != " ":
        return board[2][0]
    return None

def boardFull(board):
    for row in board:
        if " " in row:
            return False
    return True
    
def ticTacToe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Let's play!!!")
    currentPlayer = "X"

    while True:
        printBoard(board)
        
        move = input(f"Player {currentPlayer}, kindly make your move(row and column):").split()
        
        if len(move) != 2:
            print("Kindly only enter row and column with a space.")
            continue
        
        row, col = move
        if not(row.isdigit()  and col.isdigit()):
            print("Kindly enter digits only.")
            continue
       
        row, col = int(row), int(col)
        if not(0 <= row <= 2 and 0 <= col <= 2):
            print("Kindly enter digits between 0 and 2.")
            continue

        board[row][col] = currentPlayer

        winner = checkWinner(board)
        if winner:
            printBoard(board)
            print(f"Player {winner} won!")
            break

        if boardFull(board):
            printBoard(board)
            print("Alas, it's a draw!")
            break

        currentPlayer = "O" if currentPlayer == "X" else "X"

ticTacToe()

