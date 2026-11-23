class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempIndexes = deque()
        result = [None] * len(temperatures)
        for i in range(len(temperatures)):
            while tempIndexes and temperatures[tempIndexes[-1]] < temperatures[i]:
                topIndex = tempIndexes.pop()
                result[topIndex] = i - topIndex
            tempIndexes.append(i)
        for i in range(len(tempIndexes)):
            while tempIndexes:
                zeroIndex = tempIndexes.pop()
                result[zeroIndex] = 0
        return result