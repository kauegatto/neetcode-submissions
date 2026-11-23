class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for string in strs:
            for char in string:
                encoded += chr(ord(char) + 1)
            encoded += '%space'
            
        return encoded

    def decode(self, s: str) -> List[str]:
        separate = s.split('%space')
        decoded = []
        for string in separate:
            word = ''
            for char in string:
                word += chr(ord(char) - 1)
            decoded.append(word)
        decoded.pop()
        return decoded