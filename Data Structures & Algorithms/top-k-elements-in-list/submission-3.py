class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count={}
        for i in nums:
            dict_count[i]=1+dict_count.get(i,0)
        lst=[[v,k] for k,v in dict_count.items()]
        lst.sort(reverse=True)
        return [i[1] for i in lst[0:k]]
