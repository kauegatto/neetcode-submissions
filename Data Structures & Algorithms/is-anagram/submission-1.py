class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        items={}
        countdown = len(s)
        if(len(s) != len(t)):
            return False
        for i in range(len(s)):
            items[s[i]] = items.get(s[i], 0) + 1
        for j in range(len(t)):
            if(items.get(t[j], 0) > 0):
                items[t[j]] = items[t[j]] - 1
                countdown -= 1
        if (countdown==0):
            return True
        return False