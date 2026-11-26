class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        endpoints = {}
        #prefix
        for i in range(len(heights)):
            last = s[-1] if s else None
            # Stack contains (height, index)
            while last and heights[i] < last[0]:
                e = s.pop()
                endpoints[e[1]] = [-1, i]
                last = s[-1] if s else None
            s.append((heights[i], i))
        last = s[-1] if s else None
        while last:
            e = s.pop()
            endpoints[e[1]] = [-1, len(heights)]
            last = s[-1] if s else None
        #suffix
        for i in range(len(heights) -1, -1, -1):
            last = s[-1] if s else None
            # Stack contains (height, index)
            while last and heights[i] < last[0]:
                e = s.pop()
                endpoints[e[1]][0] = i
                last = s[-1] if s else None
            s.append((heights[i], i))
        m = 0
        for k, v in endpoints.items():
            m = max((v[1] - v[0] - 1) * heights[k], m)
        #print(endpoints)
        return m