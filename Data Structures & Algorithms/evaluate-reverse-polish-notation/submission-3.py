class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                op2 = stack.pop()
                op1 = stack.pop()
                result = None
                if token == "+":
                    result = op1 + op2
                elif token == "-":
                    result = op1 - op2
                elif token == "*":
                    result = op1 * op2
                else:
                    result = int(op1/op2)
                stack.append(result)
            else:
                stack.append(int(token))
            # print(stack)
        return stack[-1]
