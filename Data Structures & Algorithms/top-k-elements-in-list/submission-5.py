class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_list=[]
        dictionary={}
        for i in nums:
            dictionary[i]=1+dictionary.get(i,0)
        new_list=[[v,k] for k,v in dictionary.items()]
        new_list.sort(reverse=True)
        return [new_list[i][1] for i in range(k)]

        


        