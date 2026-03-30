class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        res=[]
        pref_arr=[]
        suff_arr=[]
        prod=1
        for i in nums:
            prod=prod*i
            pref_arr.append(prod)
        prod=1
        for i in nums[::-1]:
            prod=prod*i
            suff_arr.insert(0,prod)
        for i in range(length):
            if i==0:
                res.append(suff_arr[1])
            elif i==length-1:
                res.append(pref_arr[-2])
            else:
                res.append(pref_arr[i-1]*suff_arr[i+1])
        return res



            