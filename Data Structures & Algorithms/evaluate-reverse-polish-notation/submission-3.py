class Solution:
    
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []
        for t in tokens:
            if t == '*' or t == '-' or t == '+' or t == '/':
                t1 = s1.pop()
                t2 = s1.pop()
                if t == '*':
                    t1 = t2 * t1
                elif t == '-':
                    t1 = t2 - t1
                elif t == '+':
                    t1 = t2 + t1
                elif t == '/':
                    t1 = t2 / t1
                    t1 = int(t1)
                s1.append(t1)
            else:
                s1.append(int(t))
            
        return s1.pop()    