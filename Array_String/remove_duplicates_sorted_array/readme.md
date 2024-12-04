# Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Solution Explanation
This question is very similar to remove element, but instead of removing all occurences of a certain value, we instead remove all duplicates. Start by creating a variable which keeps track of the current value we're searching for duplicates of. If we come across a new value, current_element becomes the new value, nums[k] = nums[i], and we increment k. In the end, returning k should give use the correct number of unique elements in the array.