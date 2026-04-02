class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ''.join(char for char in s if char.isalnum())
        text = text.lower()
        reversed_text = text[::-1]
        if text == reversed_text:
            return True
        return False