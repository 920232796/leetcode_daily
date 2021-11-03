

from typing import List 


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pass 
        
        row = len(matrix)
        column = len(matrix[0])

        for r in range(0, row):
            if matrix[r][column-1] < target:
                continue
            
            for c in range(column):
                if matrix[r][c] == target:
                    return True 
            
            break 

        return False



if __name__ == "__main__":
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))