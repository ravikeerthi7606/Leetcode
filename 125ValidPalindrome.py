class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(c.lower() for c in s if c.isalnum())

        j = len(new_str) - 1
        for i in range(len(new_str) // 2):
            if new_str[i] != new_str[j]:
                return False
            j -= 1
        return True



print(Solution().isPalindrome("race a car"))