class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0 or k == 0:
            return []
        hashmap = {}
        for n in nums:
            key = n
            if key not in hashmap:
                hashmap[key] = 0
            hashmap[key] += 1
        result = sorted(hashmap, key = lambda x: hashmap[x], reverse = True)[:k]
        # result = sorted(hashmap, reverse = True)[:k]
        return result