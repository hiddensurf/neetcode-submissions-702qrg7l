class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_list=[]
        suff_list=[]
        prod=1
        for i in nums:
            prod = prod * i
            pref_list.append(prod)
        prod=1
        n=len(nums)
        for i in range(n-1,-1,-1):
            prod = prod * nums[i]
            suff_list.insert(0,prod)
        new_list=[]
        for i in range(n):
            left = pref_list[i-1] if i>0 else 1
            right = suff_list[i+1] if i<n-1 else 1
            new_list.append(left*right)
        return new_list
            
        
