class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def line_x(checked_num, x, y):
            for i in range(len(board)):
                if checked_num == board[y][i] and x != i:
                    return False
            return True
        def line_y(checked_num, x, y):
            for i in range(len(board)):
                if checked_num == board[i][x] and y != i:
                    return False
            return True
