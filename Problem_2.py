import math


def matrix_init(n):
    m = []
    for _ in range(n):
        current_row = [el for el in input().split()]
        m.append(current_row)
    return m


def check_player_position(m, n):
    for r in range(n):
        for c in range(n):
            if m[r][c] == "P":
                return r, c


size = int(input())
matrix = matrix_init(size)
current_row, current_col = check_player_position(matrix, size)
points = 0
path = []
is_dead = False
while True:
    command = input()
    if command == "up":
        if current_row > 0:
            current_row -= 1
            if matrix[current_row][current_col].isdigit():
                points += int(matrix[current_row][current_col])
            elif matrix[current_row][current_col] == "X":
                points = math.floor(points / 2)
                is_dead = True
        else:
            points = math.floor(points / 2)
            is_dead = True

    elif command == "down":
        if current_row < size - 1:
            current_row += 1
            if matrix[current_row][current_col].isdigit():
                points += int(matrix[current_row][current_col])
            elif matrix[current_row][current_col] == "X":
                points = math.floor(points / 2)
                is_dead = True
        else:
            points = math.floor(points / 2)
            is_dead = True

    elif command == "left":
        if current_col > 0:
            current_col -= 1
            if matrix[current_row][current_col].isdigit():
                points += int(matrix[current_row][current_col])
            elif matrix[current_row][current_col] == "X":
                points = math.floor(points / 2)
                is_dead = True
        else:
            points = math.floor(points / 2)
            is_dead = True

    elif command == "right":
        if current_col < size - 1:
            current_col += 1

            if matrix[current_row][current_col] == "X":
                points = math.floor(points / 2)
                is_dead = True
            else:
                current_point = matrix[current_row][current_col]
                points += int(current_point)
        else:
            points = math.floor(points / 2)
            is_dead = True
    if is_dead:
        break
    path.append([current_row, current_col])
    if points >= 100:
        break
if points >= 100:
    print(f"You won! You've collected {points} coins.")
else:
    print(f"Game over! You've collected {points} coins.")
print("Your path:")
for el in path:
    print(el)
