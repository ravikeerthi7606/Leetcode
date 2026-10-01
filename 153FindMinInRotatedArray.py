class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low+high)//2
            print(f'low: {low}, high: {high}, mid: {mid}, nums[mid]: {nums[mid]}, nums[high]: {nums[high]}')
            if nums[mid] > nums[high]:
                low = mid + 1
                print(f'low: {low}, high: {high}, mid: {mid}')
            # elif nums[mid] < nums[high]:
            #     high = mid - 1
            #     print(f'low: {low}, high: {high}, mid: {mid}')
            else:
                print(f'low: {low}, high: {high}, mid: {mid}')
                # return nums[mid]
                high = mid
        return nums[low]

print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([11,13,15,17]))
print(Solution().findMin([3,1,2]))