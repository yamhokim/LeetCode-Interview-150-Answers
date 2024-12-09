# Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

## Solution Explanation

I start by iterating through the magazine string, and creating a hash map where each key value pair is the letter and the number of times it appears.

I then iterate through the ransomNote string and check if each letter exists within the hash map. If it doesn't, I add it to the hash map with value of -1, if it does, I decrement the count of the letter by 1. If I ever get a value of -1 in the hash map, I return False. Otherwise, return True. 