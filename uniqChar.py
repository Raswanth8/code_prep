# First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        
        for c in s:
            if c not in hashmap :
                hashmap[c] = 1
            else :
                hashmap[c] += 1
        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i
        return -1