class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0]*len(temperatures)
        stack = []
        for i,num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                j = stack.pop()
                print(j)
                result[j] = i-j  
                
            stack.append(i)
            print(f'stack: {stack}, result: {result}')
        return result

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))