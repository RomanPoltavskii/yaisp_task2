def array_from_file(path):
    with open(path) as file:
        array = [[int(num) for num in line.split(' ')] for line in file]
    file.close()
    return array


# ячейка со значением "-1" — пустая
# ячейка со значением "0" — ноль
# ячейка со значением "1" — единица
'''arr = array_from_file('input.txt')
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == -1:
            print('ячейка ' + str(i) + ' ' + str(j) + " пустая" )
print(arr)'''


def check_win_of_1(board):
    for i in range(10):
        for j in range(6):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == 1:
                return 1 # найдена победа единиц

    for i in range(6):
        for j in range(10):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == 1:
                return 1 # найдена победа единиц

    for i in range(6):
        for j in range(6):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] == 1:
                return 1 # найдена победа единиц

    for i in range(6):
        for j in range(4, 10):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == board[i+4][j-4] == 1:
                return 1 # найдена победа единиц


def check_win_of_0(board):
    for i in range(10):
        for j in range(6):
            if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == 0:
                return 1 # найдена победа нулей

    for i in range(6):
        for j in range(10):
            if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == 0:
                return 1 # найдена победа нулей

    for i in range(6):
        for j in range(6):
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] == 0:
                return 1 # найдена победа нулей

    for i in range(6):
        for j in range(4, 10):
            if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == board[i+4][j-4] == 0:
                return 1 # найдена победа нулей

def solution():
    board = array_from_file('input.txt')
    win_of_0 = check_win_of_0(board)
    win_of_1 = check_win_of_1(board)

    if win_of_1 == 1 and win_of_0 != 1:
        return 1
    elif win_of_0 == 1 and win_of_1 != 1:
        return -1
    else:
        return 0


print(solution())



