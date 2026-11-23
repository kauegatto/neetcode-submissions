class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = 0
        n = len(nums)
        for i in range(n + 1):
            xorr ^= i
        for x in nums:
            xorr ^= x
        return xorr