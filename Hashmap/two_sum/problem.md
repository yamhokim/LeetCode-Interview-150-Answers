# Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 ## Solution Explanation

The idea behind the solution is to use a hash map to keep track of the elements in the array and their indices. At each step of the for loop, we calculate the associated value needed to add up to the target value.

We then check if that associated value is already in the hash map. If it is, we return the indice of the current element and the element of the associated value. 