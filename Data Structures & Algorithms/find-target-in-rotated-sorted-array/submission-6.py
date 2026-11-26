class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # get from the furthest side, 2, 1 
        # do 2 binary searches, one for the piece where this shit has been rotated
        # from there we can see if it's bigger or smaller and do another binary search

        # number 3 at idx 0 
        # find next number smaller than 3
        # if -1 we can just do binary search normally (no rotation)
        # if we always check for the left side, left means the amount the array was rotated by
        # to the left of the array, bigger numbers, to the right, smaller (invert)

        left, right = 0, len(nums) -1
        mid = -1
        while(left < right):
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
    
        # left = bigger
        ## two sorted pieces
        def binary_search(left, right):
            print(nums)
            while left <= right:
                mid = (left+right)//2
                if(target == nums[mid]):
                    return mid
                elif target > nums[mid]:
                    left = mid+1
                else:
                    right = mid -1
            return -1

        result = -1

        result = binary_search(0, left)
        if result != -1: return result 

        size = len(nums) -1
        result = binary_search(left, size)


        # right = smaller

        return result