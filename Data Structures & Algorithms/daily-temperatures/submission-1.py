class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                stackIND, stacktemp = stack.pop()
                res[stackIND] = (i-stackIND)
            stack.append((i,t))
        return res
