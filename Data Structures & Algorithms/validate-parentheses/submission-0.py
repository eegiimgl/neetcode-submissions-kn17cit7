class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch in ['(','{','['] or len(stack) == 0:
                stack.append(ch)
            else:
                if stack[-1] == '(' and ch == ')':
                    stack.pop()
                elif stack[-1] == '[' and ch == ']':
                    stack.pop()
                elif stack[-1] == '{' and ch == '}':
                    stack.pop()
                else:
                    stack.append(ch)

        print(stack)
        
        return True if len(stack) == 0 else False