class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        
        buckets = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            buckets[cnt].append(num)

        for i in range(len(buckets) -1, 0, -1):
            for item in buckets[i]:
                result.append(item)
                if len(result) == k:
                    return result
        return result
            
