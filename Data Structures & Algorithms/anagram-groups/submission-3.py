class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = defaultdict(list)
        for i in range(len(strs)):
            arr = [0] * 26
            for c in strs[i]:
                arr[ord(c) - ord('a')] += 1
            arr = tuple(arr)
            anagrams_dict[arr].append(strs[i])
        return list(anagrams_dict.values())