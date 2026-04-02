class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if j == i:
                    j += 1
                else:
                    sol[i] *= nums[j]
                    j += 1
            i += 1
        return sol