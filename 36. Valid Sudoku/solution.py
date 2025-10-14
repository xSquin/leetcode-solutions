
            for i in range(len(board)):            for i in range(len(board)):
                if checked_num == board[y][i] and x != i:                if checked_num == board[y][i] and x != i:
                    return False                    return False
            return True            return True
        def line_y(checked_num, x, y):        def line_y(checked_num, x, y):
            for i in range(len(board)):            for i in range(len(board)):
                if checked_num == board[i][x] and y != i:                if checked_num == board[i][x] and y != i:
                    return False                    return False
            return True            return True
        def square3x3(checked_num, x, y):        def square3x3(checked_num, x, y):
            for i in range(y - (y%3), y - (y%3) + 3):            for i in range(y - (y%3), y - (y%3) + 3):
                for j in range(x - (x%3), x - (x%3) + 3):                for j in range(x - (x%3), x - (x%3) + 3):
                    if checked_num == board[i][j] and i != y and j != x:                    if checked_num == board[i][j] and i != y and j != x:
                        return False                        return False
            return True            return True

        for i in range(len(board)):        for i in range(len(board)):
            for j in range(len(board)):            for j in range(len(board)):
                if board[i][j] == ".":                if board[i][j] == ".":
                    pass                    pass
                elif line_x(board[i][j], j, i) != True or line_y(board[i][j], j, i) != True or square3x3                elif line_x(board[i][j], j, i) != True or line_y(board[i][j], j, i) != True or square3x3
(board[i][j], j, i) != True:(board[i][j], j, i) != True:
                    return False                    return False
        return True        return True
                