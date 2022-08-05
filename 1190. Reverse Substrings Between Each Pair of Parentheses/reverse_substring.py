class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = ""
        for c in s:
            if c == ")":
                cur = ""
                while stk[-1] != "(":
                    cur += stk[-1]
                    stk = stk[:-1]
                stk = stk[:-1]
                cur1 = "".join(cur)
                stk += cur1
            else:
                stk += c
        return stk
