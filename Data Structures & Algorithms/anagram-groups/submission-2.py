class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices={}
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord("a")]+=1
            if tuple(count) not in indices:
                indices[tuple(count)] = []
                indices[tuple(count)].append(word)
            else:
                indices[tuple(count)].append(word)
        new_list=[]
        for lists in indices.values():
            new_list.append(lists)
        return new_list