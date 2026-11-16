class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = ({}, {})
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            s_count[sc] = s_count.get(sc, 0) + 1
            t_count[tc] = t_count.get(tc, 0) + 1
        for k, v in s_count.items():
            if k not in t_count or t_count[k] != v:
                return False
        return True