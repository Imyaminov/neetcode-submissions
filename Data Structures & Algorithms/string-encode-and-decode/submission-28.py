class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            print(s[i:j], i, j)
            length = int(s[i:j])
            i = j + 1

            result.append(s[i:length+i])

            i = i + length

        return result

