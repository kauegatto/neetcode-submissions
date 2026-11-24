class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1 # 8 items = 8 -> index 7 
        biggest = 0
        while l<=r:
            width = (r-l) ## re-check
            height = min(heights[l], heights[r])
            calc = width * height
            biggest = max(biggest, calc)
            if heights[l] < heights[r]:
                l+=1
            else: # r is bigger, r==l, in any case if we r-- it stops the loop if they're equal
                r-=1
        return biggest