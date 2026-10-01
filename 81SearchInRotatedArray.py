class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2

            if nums[mid] == target:
                return True
            
            #left side is sorted
            if nums[low] < nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1

            #right side is sorted
            elif nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[low] == nums[mid]:
                low += 1
            elif nums[high] == nums[mid]:
                high -= 1
            
        return False

print(Solution().search([2,5,6,0,0,1,2], 0))
print(Solution().search([2,5,6,0,0,1,2], 3))
print(Solution().search([1,0,1,1,1], 0))
