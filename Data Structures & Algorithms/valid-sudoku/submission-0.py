class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set, col_set, box_set = {}, {}, {}

        ROWS, COLS = len(board), len(board[0])

        for r, rval in enumerate(board):
            for c, cval in enumerate(board[r]):
                val = board[r][c]
                if val == '.':
                    continue
                
                if r not in row_set:
                    row_set[r] = set()
                if c not in col_set:
                    col_set[c] = set()
                
                box_key = 'x'.join([str(r // 3),str(c // 3)])
                if box_key not in box_set:
                    box_set[box_key] = set()

                if val in row_set[r]:
                    return False
                else:
                    row_set[r].add(val)

                if val in col_set[c]:
                    return False
                else:
                    col_set[c].add(val)

                if val in box_set[box_key]:
                    return False
                else:
                    box_set[box_key].add(val)

        return True