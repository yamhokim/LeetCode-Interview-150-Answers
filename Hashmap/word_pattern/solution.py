class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_maps = {}
        s_maps = {}

        s_words = s.split()

        if len(s_words) != len(pattern):
            return False

        for i in range(len(pattern)):
            s_word = s_words[i]
            pattern_c = pattern[i]
            
            if (s_word in s_maps.keys() and s_maps[s_word] != pattern_c) or (pattern_c in pattern_maps.keys() and pattern_maps[pattern_c] != s_word):
                return False

            pattern_maps[pattern_c] = s_word
            s_maps[s_word] = pattern_c
            

        return True