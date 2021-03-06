class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(i, j, k, visited):
            if k == len(word):
                return True
            
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i, tmp_j = x + i, y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and (tmp_i, tmp_j) not in visited \
                and board[tmp_i][tmp_j] == word[k]:
                    visited.add((tmp_i, tmp_j))
                    if helper(tmp_i, tmp_j, k+1, visited):
                        return True
                    visited.remove((tmp_i, tmp_j))
            return False
        
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and helper(i, j, 1,{(i, j)}):
                    return True
        return False