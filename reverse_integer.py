class Solution:
    def reverse(self, x: int) -> int:
        str1 = str(x)
        if str1.startswith('-'):
            reverse = int('-' + str1[:0:-1])
        else:
            reverse = int(str1[::-1])
        return reverse

print(Solution().reverse(123))  # Output: 321