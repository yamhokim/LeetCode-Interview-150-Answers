class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for i in range(len(strs)):
            char_counts = [0] * 26

            for c in strs[i]:
                index = ord(c) - ord('a')
                char_counts[index] += 1
            
            if tuple(char_counts) not in hash_map.keys():
                hash_map[tuple(char_counts)] = [strs[i]]
            else:
                hash_map[tuple(char_counts)].append(strs[i])
        
        return list(hash_map.values())

class SecondSolution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for i in range(len(strs)):
            char_counts = [0] * 26

            for c in strs[i]:
                index = ord(c) - ord('a')
                char_counts[index] += 1
            
            if tuple(char_counts) not in hash_map.keys():
                hash_map[tuple(char_counts)] = [strs[i]]
            else:
                hash_map[tuple(char_counts)].append(strs[i])
        
        return list(hash_map.values())