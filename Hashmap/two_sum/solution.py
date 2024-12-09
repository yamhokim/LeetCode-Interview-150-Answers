class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_map = {}
        for i in range(len(nums)):
            associated_value = target - nums[i]
            
            if associated_value in pair_map.keys():
                return [i, pair_map[associated_value]]

            pair_map[nums[i]] = i
