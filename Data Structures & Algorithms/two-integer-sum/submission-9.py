class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary={}
        for i,j in enumerate(nums):
            dictionary[j] = i
        for i in range(len(nums)):
            num2=target - nums[i]
            if num2 in dictionary and dictionary[num2] != i:
                return [i,dictionary[num2]]