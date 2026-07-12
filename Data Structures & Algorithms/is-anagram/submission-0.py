class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countsS = {}
        countsT = {}
        if len(t) != len(s):
            return False
        for char in s:
            if char in countsS:
                countsS[char] += 1
            else:
                countsS[char] = 1
        for char in t:
            if char in countsT:
                countsT[char] += 1
            else:
                countsT[char] = 1
        if countsT == countsS:
            return True
        return False
