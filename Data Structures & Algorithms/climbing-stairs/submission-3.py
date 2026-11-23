class Solution:
    def climbStairs(self, n: int) -> int:
        # a. 1 step remaining -> 1 way of climbinh
        # b. 2 steps remaining -> 2 ways of climbing
        # c. 3 steps -> a+b
        # d. 4 steps -> c+a
        self.stepsToAmount = {1:1, 2:2}
        return self.calculate(n)


    def calculate(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2: 
            return 2
        
        minusOne = 0
        if n-1 in self.stepsToAmount:
            minusOne = self.stepsToAmount[n-1]
        else:
            minusOne = self.calculate(n-1)
            self.stepsToAmount[n-1] = minusOne
        
        minusTwo = 0
        if n-2 in self.stepsToAmount:
            minusTwo = self.stepsToAmount[n-2]
        else:
            minusTwo = self.calculate(n-2)
            self.stepsToAmount[n-2] = minusTwo


        return minusOne + minusTwo