class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        starts = defaultdict(list)
        for i in num_set:
            if i-1 not in num_set:
                starts[i+ 1].append(i)
        m = 0
        for k in starts:
            i = k
            while i in num_set:
                i += 1
            m = max(m, i - k + 1)
        
        return m