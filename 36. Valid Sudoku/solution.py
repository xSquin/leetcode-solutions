class Solution(object):class Solution(object):
    def isValidSudoku(self, board):    def isValidSudoku(self, board):
        """        """
        :type board: List[List[str]]        :type board: List[List[str]]
        :rtype: bool        :rtype: bool
        """        """
        def line_x(checked_num, x, y):        def line_x(checked_num, x, y):
            for i in range(len(board)):            for i in range(len(board)):
                if checked_num == board[y][i] and x != i:                if checked_num == board[y][i] and x != i:
                    return False                    return False
            return True            return True
        def line_y(checked_num, x, y):        def line_y(checked_num, x, y):
            for i in range(len(board)):            for i in range(len(board)):
                if checked_num == board[i][x] and y != i:                if checked_num == board[i][x] and y != i:
                    return False                    return False
            return True            return True
