class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for n in list(s):
            if n in ('(', '[', '{'):
                stack.append(n)
                continue
            if len(stack) == 0:
                return False
            top = stack[-1]
            if n == ')' and top == '(':
                stack.pop()
            elif n == '}' and top == '{':
                stack.pop()
            elif n == ']' and top == '[':
                stack.pop()
            else:
                return False
        return len(stack) == 0
