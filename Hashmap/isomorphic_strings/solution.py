class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s2t = {}
        mapping_t2s = {}

        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if (s_char in mapping_s2t.keys() and mapping_s2t[s_char] != t_char) or (t_char in mapping_t2s.keys() and mapping_t2s[t_char] != s_char):
                return False

            mapping_s2t[s_char] = t_char
            mapping_t2s[t_char] = s_char

        return True