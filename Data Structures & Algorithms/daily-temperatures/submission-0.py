class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        count = 0
        s = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            l = s[-1][0] if s else None
            count += 1
            while l and t > l:
                popped = s.pop()
                res[popped[2]] = count - popped[1]
                l = s[-1][0] if s else None
            s.append((t, count, i))
        return res
            