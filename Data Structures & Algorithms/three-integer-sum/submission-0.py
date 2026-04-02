class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [[nums[0], nums[1], nums[2]]]
            else:
                return []
        sol = []
        nums.sort()

        for i,a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        
        return sol