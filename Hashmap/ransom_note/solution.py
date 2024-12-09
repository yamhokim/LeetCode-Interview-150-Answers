class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        words_dict = {}

        for i in range(len(magazine)):
            if magazine[i] not in words_dict.keys():
                words_dict[magazine[i]] = 1
            else:
                words_dict[magazine[i]] += 1
            print(words_dict)
        
        for i in range(len(ransomNote)):
            if ransomNote[i] not in words_dict.keys():
                words_dict[ransomNote[i]] = -1
            else:
                words_dict[ransomNote[i]] -= 1

            print(words_dict)
            
            if words_dict[ransomNote[i]] == -1:
                return False

        return True
        
solution = Solution()
print(solution.canConstruct('aa', 'aab'))