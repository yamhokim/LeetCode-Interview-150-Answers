# Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

## Solution Explanation
The key to solving this in O(n) time with O(1) space complexity is to start filling in the nums1 array from the last index to index m. Essentially create three pointers, one pointing to the last index of nums1 (m + n - 1), one pointing at the last filled index of nums1 (m - 1), and one pointing at the last index of nums2 (n - 1). Then basically compare num1[m-1] to nums2[n-1]. If the value from nums1 is greater, put it at nums1[last], then decrement m and last. If the value from nums2 is greater, put it at nums2[last], then decrement n and last. 

Once either m or n is less than or equal to zero, we will run a second loop which will dump any remaining elements in nums2 at the start of nums1 in the order we find them, since we're guaranteed they're sorted.

The result should be the merged sorted array.