class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        
            res = []
            i = 0
            while i < len(s):
                # 1. Find the '#' manually to get the length
                j = i
                while s[j] != "#":
                    j += 1
                
                # 2. Extract the length (the part between the old i and the current j)
                length = int(s[i:j])
                
                # 3. Skip the '#' and extract the actual string
                i = j + 1
                res.append(s[i : i + length])
                
                # 4. Move i forward to the start of the next length marker
                i += length
                
            return res