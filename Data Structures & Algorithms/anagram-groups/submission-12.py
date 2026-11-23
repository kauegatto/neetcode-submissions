class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordsToList = defaultdict(list)
        charStart = ord('a')
        for word in strs:
            charCount = list([0] * 26)
            for c in word:
                position = charStart - ord(c) # difference between char and a -> a = 64, b=65 b-a=1 (index 1)
                charCount[position] +=1
            wordsToList[tuple(charCount)].append(word)
        return list(wordsToList.values())