class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        remove =list(set(nums))
        underscore = len(nums) - len(remove)
        k = len(remove)
        
        return remove

print(Solution.removeDuplicates(nums=[1,1,2]))