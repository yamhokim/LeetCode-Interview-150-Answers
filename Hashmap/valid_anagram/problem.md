# Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

## Solution Explanation

The first solution involves creating to hash maps, one for t and one for s. The key-value pairs in the hash map are the character and its associated count. After getting these, we compare the counts of each letter, if they ever are not equal, we return False. We also return False if the two strings are not the same length. Else, we return True.

The second solution involves sorting both strings by letters, then seeing if they're equal. Only return True if both strings are equal.