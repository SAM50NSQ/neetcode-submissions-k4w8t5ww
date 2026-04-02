class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        elif s == t:
            return True 
        return self.answer(s, t)
        
    def answer(self, s, t):
        if len(s) == 0:
            return True
        for i, S in enumerate(s):
            for j, T in enumerate(t):
                if S == T:
                    print(S, T)
                    return self.answer(s[i+1:], t[j+1:])
                if j == len(t) - 1:
                    return False
        return False