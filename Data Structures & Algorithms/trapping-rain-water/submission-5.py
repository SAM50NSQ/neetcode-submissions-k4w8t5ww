class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        l = 0
        r = l + 1
        water = 0
        total = 0
        rev_test = True
        max = l
        while r < len(height):
            if height[r] >= height[l]:
                total += water
                water = 0
                l = r
                max = l
            elif height[r] < height[l]:
                water += height[l] - height[r]
            r += 1
        if rev_test == True:
            print("reverse")
            check = height[max:]
            total += Solution().trap(check[::-1])
        return total