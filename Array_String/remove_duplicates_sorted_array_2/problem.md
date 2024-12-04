# Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## Solution Explanation
This is kind of similar to the solution for remove duplicates from sorted array I. Instead, k now starts at 1, since we know the first element in the array will always be included in the final array. The main check now is basically comparing nums at index i to nums at index k - 2. This essentially looks 2 elements before, so if those two match, it means that there are already two of the element in the array and the 3rd duplicate must be "removed" from the array.