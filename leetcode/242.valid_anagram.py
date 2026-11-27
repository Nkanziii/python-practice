class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for char in s:
            if char in count_s:
                count_s[char] += 1
            else:
                count_s[char] = 1
        
        for lett in t:
            if lett in count_t:
                count_t[lett] += 1
            else:
                count_t[lett] = 1
        
        return count_s == count_t