class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc += str(len(s))+" "+s
        return enc
    def decode(self, s: str) -> List[str]:
        dec = []
        j = -1
        m = 0
        num = ""
        b = ""
        for i in range(len(s)):
            if m > 0:
                dec[j] += s[i]
                m -= 1
            else:
                if s[i] == " ":
                    m = int(num)
                    num = ""
                    dec.append("")
                    j += 1
                else:
                    num += s[i]
        return dec
