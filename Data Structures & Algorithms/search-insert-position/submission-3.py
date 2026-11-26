class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Cases: 
            1. empty array
            2. 1-indexed array
            3. array with the data we need
            4. array without the data
        '''

        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = (left + right) // 2 ## mid = left + (right - left) // 2 avoids overflow
            midNumber = nums[mid]

            if midNumber == target:
                return mid
            elif midNumber < target:
                left = mid + 1
            elif midNumber > target:
                right = mid -1

        if target > midNumber:
            return mid + 1
        else:
            return max(0,mid)

        return mid
