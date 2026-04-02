class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1 = 0
        index2 = 0

        for i, n in enumerate(numbers):
            for j in range(i+1, len(numbers)):
                if (n + numbers[j]) == target:
                    index1 = i + 1
                    index2 = j + 1
                    return [index1, index2]