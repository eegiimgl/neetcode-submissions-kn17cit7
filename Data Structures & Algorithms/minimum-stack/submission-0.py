class MinStack:

    def __init__(self):
       self.main_stack = []
       self.min_stack = [] 

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = min(self.min_stack[-1], val)
            self.min_stack.append(min_val)


    def pop(self) -> None:
        if self.main_stack:
            self.main_stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1] if self.main_stack else None

    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
