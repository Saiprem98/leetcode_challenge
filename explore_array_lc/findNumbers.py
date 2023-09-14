class Solution(object):
    def findEven(self,num):
        count = 0
        value = num 
        while(value != 0):
            value = value // 10
            count += 1
            
        return count%2==0
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for num in nums:
            if(self.findEven(num)):
                ans += 1
        return ans
        