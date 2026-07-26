class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency={}
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        freq_list=[[v,k] for k,v in frequency.items()]
        freq_list.sort(reverse=True)
        return [freq_list[i][1] for i in range(k)]
