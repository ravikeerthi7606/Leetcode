class Solution:
    def isPalindrome(x: int) -> bool:
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
          return False

sol = Solution
val1 = sol.isPalindrome(45)
print(val1)

def palindrome(x):
    str1 = str(x)
    lst = [True if str1 == str1[::-1] else False][0]
    return lst 

print(palindrome(45))
