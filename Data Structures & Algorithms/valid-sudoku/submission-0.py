class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row={}
        for i in range(9):
            row[i]=[]
        col={}
        for i in range(9):
            col[i]=[]
        box={}
        for i in range(3):
            for j in range(3):
                box[(i,j)]=[]
        for row_num in range(9):
            for col_num in range(9):
                element=board[row_num][col_num]
                if element==".":
                    continue
                if element in row[row_num]:
                    return False
                else:
                    row[row_num].append(element)
                if element in col[col_num]:
                    return False
                else:
                    col[col_num].append(element)
                if element in box[(row_num//3,col_num//3)]:
                    return False
                else:
                    box[(row_num//3,col_num//3)].append(element)
        return True



                