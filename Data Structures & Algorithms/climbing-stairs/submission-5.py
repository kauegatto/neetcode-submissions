class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return 2
        tabulation = [-1] * n
        # 0 -> n-1 spaces.
        tabulation[0] = 1 # step 0
        tabulation[1] = 2 # step 1
        for i in range(2,n):
            tabulation[i] = tabulation[i-1] + tabulation[i-2]
        return tabulation[n-1]