
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    pass
                elif line_x(board[i][j], j, i) != True or line_y(board[i][j], j, i) != True or square3x3
(board[i][j], j, i) != True:
                    return False
        return True
        
