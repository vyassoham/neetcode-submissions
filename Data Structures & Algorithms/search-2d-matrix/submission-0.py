import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target in np.ravel(matrix):
            return True
        else :
            return False        
        