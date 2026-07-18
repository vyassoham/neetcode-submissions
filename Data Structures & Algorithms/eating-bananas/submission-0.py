import math
from typing import List 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            if sum(math.ceil(p / k) for p in piles) <= h:
                r = k
            else:
                l = k + 1
        return l    


        