class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = [1] * len(nums)
        for i, n in enumerate(nums):
            if i < len(nums)-1:
                sol[i+1] = sol[i] * n
        post = 1
        j = len(nums) - 1
        while j >= 0:
            sol[j] *= post
            post *= nums[j]
            j -= 1
        return sol