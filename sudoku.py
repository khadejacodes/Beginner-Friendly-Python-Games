import numpy 

grid = list()
for i in range(0,9):
    row = list()
    print(f"ROW NUMBER {i+1}:")
    for j in range(0,9):
        num = int(input("Enter the number:"))
        row.append(num)
    grid.append(row)

print(numpy.matrix(grid))

def possible(number, row, column, grid):
    for i in range(0, 9):
        if grid[row][i] == number or grid[i][column] == number:
            return False

    initialRow = (row // 3) * 3
    initialColumn = (column // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[initialRow + i][initialColumn + j] == number:
                return False

    return True

def sudokuSolver():
    global grid
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if possible(n, i, j, grid):
                        grid[i][j] = n
                        sudokuSolver()
                        grid[i][j] = 0
                return
    print(numpy.matrix(grid))                
    print("Solved the puzzle!")                                 

sudokuSolver()    