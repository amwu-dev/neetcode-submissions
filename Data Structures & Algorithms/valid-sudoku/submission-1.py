class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                item = board[i][j]
                if item in rows[i]:
                    return False
                rows[i].add(item)
                if item in columns[j]:
                    return False
                columns[j].add(item)
                if item in squares[(i // 3, j // 3)]:
                    return False
                squares[(i //3, j //3)].add(item)
        return True