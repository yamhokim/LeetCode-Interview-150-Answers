# Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

Each letter in pattern maps to exactly one unique word in s.
Each unique word in s maps to exactly one letter in pattern.
No two letters map to the same word, and no two words map to the same letter.

# Solution Explanation

The solution here is very similar to the question about isomorphic strings. Essentially, create two hashmaps which house mappings either way, from a letter in pattern to the word in s and vice versa. The only things to consider is splitting the string s into an array where each element is an individual word, and also the fact that we're not guaranteed that there are the same number of letters and words.