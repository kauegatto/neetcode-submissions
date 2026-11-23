class Solution:
    def isValid(self, s: str) -> bool:
        openings = ['(', '{', '[']
        closings = [']', '}', ')']
        
        closingToOpening = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        # openingStack 
        
        # ( -> stack = (
        # ) -> if stack is not empty -> stack.pop() -> see if popped value is closingToOpening[')']
        # if not return false
        # at the end, stack len must be 0 (no left opening)
        
        openingStack = []

        for c in s:
            if c in openings:
                openingStack.append(c)
            elif c in closings:
                if not openingStack: # no matching opening
                    return False

                opening = openingStack.pop()
                if opening != closingToOpening[c]:
                    return False
        return len(openingStack)==0