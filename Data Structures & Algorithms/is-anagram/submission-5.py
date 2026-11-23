class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}
        
        if(len(s) != len(t)):
            return False

        for character in s:
            word1[character] = word1.get(character,0)+1
        for character in t:
            word2[character] = word2.get(character,0)+1
        for character in t:
            if(word1.get(character,0) != word2.get(character,0)):
                return False
        return True