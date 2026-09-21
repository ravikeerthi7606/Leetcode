class Solution:
    def findMedianSortedArrays(nums1, nums2) -> float:
        sorted = nums1 +nums2
        sorted.sort()


        length = len(sorted)
        if (length % 2) == 0:
            print(sorted)
            ans =(sorted[length//2]+sorted[length//2-1])/2
            return float(ans)
        elif (length%2) == 1:
            print(sorted)
            ans = sorted[length//2]
            return float(ans)

        # print(sorted)


sol = Solution
val1 = sol.findMedianSortedArrays([1,2],[3,4])
print(val1)