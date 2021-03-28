class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:

        d = {}
        for (k, v) in knowledge:
            d[k] = v

        N = len(s)

        res = ""

        k = ""
        opened = False
        for i in range(len(s)):
            c = s[i]

            if c == "(":
                opened= True
            elif c == ")":
                opened = False
                val = d.get(k, "?")
                res += val
                k = ""
            else:
                if opened:
                    k += c
                else:
                    res += c

        return res

