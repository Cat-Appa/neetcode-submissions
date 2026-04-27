class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for x in operations:
            if x == "+":
                ans.append(ans[-1] + ans[-2])
            elif x == "D":
                ans.append(ans[-1] * 2)
            elif x == "C":
                ans.pop()
            else:
                ans.append(int(x))
        return sum(ans)
