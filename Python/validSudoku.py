def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    ver={}
    box={}
    for i in range(9):
        hor={}
        for m in range (9):
            if board[i][m].isalnum():
                ver[(m, board[i][m])] = ver.get((m, board[i][m]), 0)+1
                box[(i//3, m//3, board[i][m])] = box.get((i//3, m//3, board[i][m]), 0)+1
                hor[board[i][m]] = hor.get(board[i][m], 0)+1
                if hor[board[i][m]]>1 or ver[(m, board[i][m])]>1 or box[(i//3, m//3, board[i][m])] >1: return False
    return True
                