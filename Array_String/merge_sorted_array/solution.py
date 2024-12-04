class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Create three pointers, one pointing at the last spot of nums1,
        # one pointing at the m - 1 index of nums1, and one pointing at
        # the n - 1 index of nums2
        last = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            elif nums2[n-1] > nums1[m-1]:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
        


