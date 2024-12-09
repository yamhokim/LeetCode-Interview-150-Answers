# Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

**Follow-up**: Could you solve the problem in linear time and in O(1) space?

## Solution Explanation

For the first solution, the entire idea is to create a hashmap containing all the counts associated with each element in the array. Everytime an element is occured, we add 1 to its associated count in the hash map. If the count of the element ever exceeds the current maxCount, the maxCount is set as that element's count, and the majority element, so far, is set as that current element. The majority element we return at the end should then be the overall majority element in the array.

For the better solution with O(n) runtime and O(1) space complexity, we don't use a hash map at all. Instead, we have one variable to keep track of the majority element so far, and one variable for keeping track of the count. If the current element matches the current majority element, we increment the count. However, if the element does not match, we decrement the count. However, if the current count is zero, we now set the current element as the majority element and increment the counter. This is because the previous element is not the majority element so far. In the end, the overall majority element is returned.