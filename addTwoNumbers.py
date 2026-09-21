class Solution:
    def addTwoNumbers(l1,l2) :
        # L1 = l1[::-1]
        # L2 = l2[::-1]
        # print(L1,L2)

        if len(l1) != len(l2):
            find_len = max(len(l1),len(l2)) - min(len(l1),len(l2))
            L1 = max(l1,l2)
            L2 =  min(l1,l2)
            for i in range(find_len):
                L2.append(0)
            ans = []
            for i in range(len(L1)):
                ans.append(L1[i]+L2[i])
            return ans 
        
        else:
            ans = []
            for i in range(len(l1)):
                add = l1[i]+l2[i]
                if add>9:
                    ans.append(add-10)
                    # ans.append(l1)
                carry = 1
                ans.append(add)
            return ans 


            

sol = Solution
a=sol.addTwoNumbers([9,9,9,9,9,9,9],[9,9,9,9])
print(a)

b= sol.addTwoNumbers([2,4,3],[5,6,4])
print(b)

c = sol.addTwoNumbers([0],[0])
print(c)