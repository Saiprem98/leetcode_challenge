class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        length_ = len(arr) - 1
        poss_dup = 0 

        for i in range(length_):
            if i > length_ - poss_dup:
                break
            
            if arr[i] == 0:
                if i == length_ - poss_dup:
                    arr[length_ ] = 0
                    length_ -=1 
                    break
                poss_dup +=1
        
        last = length_ - poss_dup

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + poss_dup] = 0
                poss_dup -=1
                arr[i + poss_dup] = 0
            else: 
                arr[i + poss_dup] = arr[i]