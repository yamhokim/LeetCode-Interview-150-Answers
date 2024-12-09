class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority_element = 0
        maxCount = 0

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

            if counts[num] > maxCount:
                majority_element = num
                maxCount = counts[num]

        return majority_element
    

class BetterSolution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority_element = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != majority_element and count > 0:
                count -= 1
            elif nums[i] != majority_element and count == 0:
                majority_element = nums[i] 
                count += 1
            else:
                count += 1

        return majority_element