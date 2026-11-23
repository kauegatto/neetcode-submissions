class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        d = {i: i for i in range(len(nums) + 1)} # 0 -> 23
        for i in range(0, len(nums)):
            d.pop(nums[i])
        return list(d.keys())[0]