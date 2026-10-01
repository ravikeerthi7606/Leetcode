class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers)-1

        while low < high:
            add = numbers[low] + numbers[high]
            if add == target:
                return [low+1, high+1]
            elif add < target:
                low +=1
            else:
                high -=1
            

print(Solution().twoSum([2,7,11,15], 9))