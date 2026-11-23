class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        while start <= end:
            if not isAlphaNumeric(s[start]):
                start += 1
                continue
            if not isAlphaNumeric(s[end]):
                end -= 1
                continue
                
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

def isAlphaNumeric(s:str) -> bool:
    ## a-z
    if 97 <= ord(s) <= 122:  ## a-z
        return True
    elif 65 <= ord(s) <= 90:  ## A-Z
        return True
    elif 48 <= ord(s) <= 57: ## 0-9
        return True
    else:
        return False