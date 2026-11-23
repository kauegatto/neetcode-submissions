class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all = set(nums)
        if len(all) != len(nums):
            return True
        return False
