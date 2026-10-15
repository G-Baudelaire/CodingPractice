class Solution(object):
    BOARD_SIZE = 9

    def __init__(self):
        self.board = None

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        self.board = board

        if self._areRowsValid() and self._areColumnsValid() and self._areSubBoxesValid():
            return True
        return False

    def _areRowsValid(self):
        rows = (self._getRow(i) for i in range(self.BOARD_SIZE))
        return self._areSectionsValid(rows)

    def _areColumnsValid(self):
        columns = (self._getColumn(i) for i in range(self.BOARD_SIZE))
        return self._areSectionsValid(columns)

    def _areSubBoxesValid(self):
        sub_boxes = (self._getSubBox(i) for i in range(self.BOARD_SIZE))
        return self._areSectionsValid(sub_boxes)

    def _areSectionsValid(self, sections):
        for section in sections:
            if not self._isSectionValid(section):
                return False
        return True

    def _isSectionValid(self, section):
        for number in set(section).difference({"."}):
            if 1 != section.count(number):
                return False
        return True

    def _getRow(self, row_index):
        return self.board[row_index]

    def _getColumn(self, column_index):
        return [self.board[i][column_index] for i in range(self.BOARD_SIZE)]

    def _getSubBox(self, sub_box_index):
        top_left_index = self._threeByThree1DTo2D(sub_box_index)
        sub_box = [0] * 9
        for i in range(self.BOARD_SIZE):
            offset = self._getOffset(i)
            sub_box[i] = self._boardValueFromTopLeftAndOffset(top_left_index, offset)
        return sub_box

    def _threeByThree1DTo2D(self, sub_box_index):
        return (sub_box_index // 3) * 3, (sub_box_index % 3) * 3

    def _getOffset(self, value):
        return value // 3, value % 3

    def _boardValueFromTopLeftAndOffset(self, top_left, offset):
        row = top_left[0] + offset[0]
        column = top_left[1] + offset[1]
        return self.board[row][column]


test_board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(Solution().isValidSudoku(test_board))
