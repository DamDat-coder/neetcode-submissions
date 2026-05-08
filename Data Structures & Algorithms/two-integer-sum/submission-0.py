class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            subtrahend = target - num

            if subtrahend in seen:
                return [seen[subtrahend], i]

            seen[num] = i

