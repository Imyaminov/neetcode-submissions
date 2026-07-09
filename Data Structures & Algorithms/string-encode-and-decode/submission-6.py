class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for item in strs:
            result += item+str(len(item))[-1]+"&"
        return result

    def decode(self, s: str) -> List[str]:
        result = []             
        element = ""

        for idx in range(len(s)):
            if s[idx] == "&" and s[idx-1].isdigit():
                element = element[:-1]
                result.append(element)
                element = ""
                continue
            element += s[idx]
        return result