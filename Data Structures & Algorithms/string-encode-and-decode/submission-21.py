class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        l = ''
        pivot = i = 0
        print(s)
        while i < len(s):
            if s[i].isdigit():
                l += s[i]
                i+=1
            if s[i] == "#":
                print(l)
                if l.isdigit():
                    result.append(s[i+1:i+int(l)+1])
                    pivot = i+int(l)+1
                l = ''
                i = pivot
        return result