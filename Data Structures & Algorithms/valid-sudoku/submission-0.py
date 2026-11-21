class Solution:
    def checkDuplicate(self, row: List) -> bool:
        rmap = defaultdict(int)
        for r in row:
            rmap[r] += 1
            if rmap[r] > 1 and r != '.':
                return True
            print(r)
        print(" row done")
        return False

    def checkDuplicateColumn(self, board, i) -> bool:
        cmap = defaultdict(int)
        for c in range(9):
            cmap[board[c][i]] += 1
            if cmap[board[c][i]] > 1 and board[c][i] != '.':
                return True
            print(board[c][i])
        print(" column done")
        return False

    def checkDuplicateThreeByThree(self, board, i, j):
        m = defaultdict(int)
        for x in range(i * 3, i * 3 + 3):
            for y in range(j * 3, j * 3 + 3):
                print(board[x][y])
                m[board[x][y]] += 1
                if board[x][y] != '.' and m[board[x][y]] > 1:
                    return True
        print(i, j, 'Done')
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        rows = {}
        for i in range(9):
            if self.checkDuplicate(board[i]):
                return False
        # Check columns
        for i in range(9):
             if self.checkDuplicateColumn(board, i):
                return False
        # Check subgrids
        for i in range(3):
            for j in range(3):
                if self.checkDuplicateThreeByThree(board, i, j):
                    return False
        return True