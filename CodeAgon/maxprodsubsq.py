# Maximum Product of the Length of Two Palindromic Subsequences
"""
Input: s = "leetcodecom"
Output: 9
Explanation: An optimal solution is to choose "ete" for the 1st subsequence and "cdc" for the 2nd subsequence.
The product of their lengths is: 3 * 3 = 9.

Use BitMask, find the subsequence, perform and operation and find max product.

"""
class Solution:
    def maxProduct(self, s: str) -> int:
        N, hashP = len(s),{} # mask : length
        
        for mask in range(1,2**N):
            subseq = ""
            for i in range(N):
                if(mask & (1 << i)):
                    subseq += s[i] # order would be same both ways
            if subseq == subseq[::-1]:
                hashP[mask] = len(subseq)
        res = 0
        for a in hashP:
            for b in hashP:
                if (a & b == 0):
                    res = max(res,hashP[a]*hashP[b])
        return res