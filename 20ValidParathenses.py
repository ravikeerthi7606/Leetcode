class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(':')', '[':']', '{':'}'}
        stack = []
        for ch in s:
            if ch in ')]}' and stack and pairs[stack[-1]] == ch:
                stack.pop()
            else:
                stack.append(ch)
            print(stack)
        return len(stack) == 0



print(Solution().isValid('{([)]}{}'))
