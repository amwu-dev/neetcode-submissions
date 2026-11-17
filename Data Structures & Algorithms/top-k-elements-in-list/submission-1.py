class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        bucket = defaultdict(list)
        for i in nums:
            d[i] += 1
        m = 0
        ret = []
        for key, v in d.items():
            bucket[v].append(key)
            m = max(v, m)
        i = 0
        f = 0
        while i < k:
            j = 0
            target = m - f
            if target in bucket: 
                while j < len(bucket[target]) and i < k:
                    ret.append(bucket[target][j])
                    i += 1
                    j += 1
            f += 1
        return ret