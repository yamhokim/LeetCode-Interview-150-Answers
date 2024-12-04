# Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


## Solution Explanation
Start by removing all non-alphanumeric characters then converting all letters to lowercase. Initialize two pointers, one pointing at the start and the other at the end. Keep incrementing and decrementing the start and end pointers, respectively, until they cross each other, and check whether the values are equal at each step. If they are ever unequal, return False, as this is not a valid palindrome. If the entire loop finishes, it indicates a valid palindrome so return True.