# Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Solution Explanation
For this question, use two pointers. One pointer is K, which signifies where the non-val number will be placed while the other pointer is i, which represents the current number we're looking at. If nums[i] is not equal to val, then we want to place nums[i] at wherever k is pointing two. Then we increment both k and i. If nums[i] is equal to val, don't increment k, simply only increment i. 

This solution will not only sort the list by putting all val numbers at the end, but the value of k will end up as the number of non-val numbers in the array nums.