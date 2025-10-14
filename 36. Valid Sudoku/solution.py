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
                
