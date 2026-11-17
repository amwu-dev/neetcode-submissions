class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(': ')', '{' : '}', '[':']'}
        to_check = set(['(', '{', '['])
        for c in s:
            if c in to_check:
                stack.append(d[c])
            else:
                if len(stack) == 0 or stack.pop() != c:
                    return False
        return len(stack) == 0