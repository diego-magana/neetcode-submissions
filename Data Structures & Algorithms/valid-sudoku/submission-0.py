'''
Intuition
A board is valid if no digit repeats within any row, any column, or any 3x3 box.
Empty cells (".") are ignored, and the board doesn't have to be solvable. 
Scan every cell once. 
For each digit, 3 questions: has this row, this column, or this box already seen it?
If yes, the board is invalid. 
If no, record the digit in all three and continue. 

Key structures: one set of seen digits per row, per column, and per box. 
    rows[r]           -> digits seen in row c
    cols[c]           -> digits seen in column c
    squares[(br, bc)] -> digits seen in box (br, bc)

Box indexing: integer-divide by 3 to map a cell to its box. 
r // 3 and c // 3 each give 0, 1, or 2, so (r // 3, c // 3)
names one of 9 boxes:
    rows 0-2 -> box row 0     cols 0-2 -> box col 0
    rows 3-5 -> box row 1     cols 3-5 -> box col 1
    rows 6-8 -> box row 2     cols 6-8 -> box col 2
e.g. cell (4, 7) -> (4 // 3, 7 // 3) = (1, 2): the middle-right box

Time: O(81) = O(1) for a fixed 9x9 board (O(n**2)) for an n x n board)
Space: O(81) = O(1); each set holds at most 9 digits
Trace below: a board whose only filled cells are
    (0,0)="5", (0,4)="7", (1,1)="5"   -> invalid: two 5s in the top-left box
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # defaultdict(set): looking up a missing key creates an empty set,
        # so rows[r], cols[c] and squares[...] can be checked with 'in'
        # or .add()'d to immediately w/ no 'if key not in' setup.
        # Sets give O(1) checks, same idea as hash maps.
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # key is a TUPLE (box_row, box_col)
                                    # tuple is hashable so works as a key

        # Visit every cell: r = row 0-8, c = column 0-8 (81 cells total).
        for r in range(9):
            for c in range(9):
                # Empty cell: nothing to validate. Continue to next c.
                if board[r][c] == ".":
                    continue

                # Duplicate check BEFORE recording the digit. 
                # If the digit is already in this row's, column's, or box's set, 
                # it has appeared there before, so the board is invalid. 
                # 'or' stops at the first True
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r //3, c // 3)]):
                    return False

                # No conflict: record digit in all three groups it belongs to.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        # (0,0) "5": rows[0]={}, cols[0]={}, squares[(0,0)]={}  -> no conflict
        #            rows[0]={5}, cols[0]={5}, squares[(0,0)]={5}
        # (0,1)-(0,3): "."  -> skipped
        # (0,4) "7": box (0//3, 4//3) = (0,1); rows[0]={5} has no 7 -> no conflict
        #            rows[0]={5,7}, cols[4]={7}, squares[(0,1)]={7}
        # (0,5)-(1,0): "."  -> skipped
        # (1,1) "5": rows[1]={}  -> no hit
        #            cols[1]={}  -> no hit
        #            box (1//3, 1//3) = (0,0); squares[(0,0)]={5}  -> HIT
        #            -> return False
        # (The row and column checks pass; only the box check catches this one.)

        # Every filled cell was checked with no repeats in any group.
        return True