class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        anagrams_dict = {}
        for i in range(len(strs)):
            arr = [0] * 26
            curr_str = strs[i]
            curr_dict = {}
            for c in curr_str:
                arr[ord(c) - ord('a')] += 1
            arr = tuple(arr)
            if arr not in anagrams_dict:
                anagrams_dict[arr] = len(anagrams)
                anagrams.append([curr_str])
            else:
                anagrams[anagrams_dict[arr]].append(curr_str)
        return anagrams