class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tab={}
        for i in nums:
            if i in tab:
                tab[i]=tab[i]+1
            else:
                tab[i]=1
            if tab[i] > 1:
                return True
        return False