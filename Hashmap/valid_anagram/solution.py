class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counts = {}
        t_counts = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_counts[s[i]] = 1 + s_counts.get(s, 0)
            t_counts[t[i]] = 1 + t_counts.get(t, 0)

        for char in s_counts.keys():
            if s_counts[char] != t_counts.get(char, 0):
                return False
            

        return True
    
class SecondSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)