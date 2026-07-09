from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        duplicates = defaultdict(int)
        result = []
        for num in nums:
            duplicates[str(num)] += 1

        for i in range(k):
            number = max(duplicates.items(), key=lambda item: item[1])[0]
            duplicates.pop(number)
            result.append(number)

        return result
        
            