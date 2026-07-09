class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        l = ''
        
        while i < len(s):
            if s[i].isdigit():
                l += s[i]
                i += 1
            if s[i] == "#":
                if l.isdigit():
                    result.append(s[i+1:i+1+int(l)])
                    i += 1+int(l)
                l = ''
        return result