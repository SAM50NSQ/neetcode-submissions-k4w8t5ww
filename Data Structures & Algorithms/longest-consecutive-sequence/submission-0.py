class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        heapq.heapify(nums)
        past = heapq.heappop(nums)
        flag = 1
        maxlen = 1
        while nums:
            current = heapq.heappop(nums)
            if current == past:
                continue
            elif current == (past + 1):
                flag += 1
            elif current > (past + 1):
                maxlen = max(flag, maxlen)
                flag = 1
            past = current

        return max(flag, maxlen)