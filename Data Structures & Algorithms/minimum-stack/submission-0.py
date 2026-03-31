class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # need to add this into min heap
        # to maintain the minimum order
        topval = None
        minval = None
        if len(self.stack) > 0:
            (topval, minval) = self.stack[-1]
            minval = min(val, minval)
        else:
            minval = val
        self.stack.append((val, minval))

    def pop(self) -> None:
        # todo: check if empty
        (topval, minval) = self.stack.pop()
        # todo: remove from min heap
        return topval

    def top(self) -> int:
        # todo: check if empty
        (topval,minval) = self.stack[-1]
        return topval

    def getMin(self) -> int:
        (topval,minval) = self.stack[-1]
        return minval
