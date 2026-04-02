class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            map1 = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            map2 = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
            for j in range(0,9):
                key1 = board[i][j]
                key2 = board[j][i]
                if key1 in map1:
                    map1[key1] += 1
                    if map1[key1] > 1:
                        return False
                if key2 in map2:
                    map2[key2] += 1
                    if map2[key2] > 1:
                        return False
        
        i, j = 0, 0
        while i < 3:
            while j < 3:
                maps = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0}
                k = 0
                while k < 3:
                    l = 0
                    while l < 3:
                        a = 3 * i + k
                        b = 3 * j + l
                        key = board[a][b]
                        if key in maps:
                            maps[key] += 1
                            if maps[key] > 1:
                                return False
                        l += 1
                    k += 1
                j += 1
            i += 1
        
        return True