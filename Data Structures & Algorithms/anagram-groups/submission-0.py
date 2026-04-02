class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []
        if len(strs) == 1:
            return [strs]
        sorted_strs = [""] * len(strs)
        strs = sorted(strs, key= lambda x: sorted(list(x)))
        for i, s in enumerate(strs):
            t = list(s)
            t = sorted(t)
            sorted_strs[i] = "".join(t)
        i = 0
        result = []
        while i < len(strs):
            j = i + 1
            s = [strs[i]]
            while j < len(strs) and sorted_strs[i] == sorted_strs[j]:
                    s.append(strs[j])
                    j += 1
            i = j
            result.append(s)
        return sorted(result, key=len)