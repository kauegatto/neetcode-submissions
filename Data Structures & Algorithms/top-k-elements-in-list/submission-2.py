class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap orders by the quantity
        # 9->8->7->6
        # A way to link a heap to a number?
        # Dict that for every number it returns the elements bound to it?
        # 9 9 (get the 2 first on 9) if k==2
        # We can get to it by counting for each number the amount of time it appears with  second hashmap
        numberToFrequency = defaultdict(int) # 0:5, 1:2, 2:2
        frequencyToNumbers = defaultdict(list) # 5: [0], 2: [1,2]
        for number in nums:
            oldFrequency = numberToFrequency[number] 
            numberToFrequency[number] += 1
            newFrequency = numberToFrequency[number] 
            frequencyToNumbers[newFrequency].append(number)
            if oldFrequency == 0:
                continue
            frequencyToNumbers[oldFrequency].remove(number)

        mostFrequent = list(frequencyToNumbers.keys())
        mostFrequent.sort()
        mostFrequent.reverse()

        result = []
        remainingNumbers = k
        for i in range(len(nums)):
            allNumbers = frequencyToNumbers[mostFrequent[i]]
            for number in allNumbers:
                remainingNumbers -=1
                result.append(number)
                if remainingNumbers == 0:
                    break
            if remainingNumbers == 0:
                break
        return result

        