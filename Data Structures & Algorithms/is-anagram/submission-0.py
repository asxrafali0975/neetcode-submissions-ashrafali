from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = Counter(s)
        d2 = Counter(t)
        return d1==d2
        
        