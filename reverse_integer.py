class Solution:
    def reverse(self, x: int) -> int:
        str1 = str(x)
        if str1.startswith('-'):
            rev = int('-'+str1[:0:-1])
        else:
            rev = int(str1[::-1])

        if rev <= -2**31 or rev >= 2**31 - 1:
            return 0
        else:
            return rev

        