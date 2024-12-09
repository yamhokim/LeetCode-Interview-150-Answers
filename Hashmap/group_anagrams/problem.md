# Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Solution Explanation

For my first solution, the idea was to iterate through the array of words, then sort the word and essentially group the anagrams that way by using a hashmap where the key is the sorted word, and the value is the word in the original array.
Afterwards, I'd create an array by iterating through the keys of the dictionary and appending the array associated with each key into the main array. This provides us with time complexity O(m * nlogn).
