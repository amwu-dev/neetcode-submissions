class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = 0
        for i in range(len(heights) + 1):
            top = s[-1] if s else None
            # Why the condition <=? We need to deal with duplicates. we prefer a monotonically increasing stack. The new rectangle i will replace the old one if we pop correctly since the previous top will be now the current top for the rectangle i so the area calculation is the same.
            while top is not None and (i == len(heights) or heights[i] <= heights[top]):

                current = s.pop()
                top = s[-1] if s else None
                if top is not None:
                    area = heights[current] * (i - top - 1)
                else:
                    area = heights[current] * i
                m = max(m, area)
            s.append(i)
        return m