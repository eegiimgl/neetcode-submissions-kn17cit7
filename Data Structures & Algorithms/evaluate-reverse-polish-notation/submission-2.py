class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(token)
            else:
                operand1 = int(stack.pop())
                operand2 = int(stack.pop())
                if token == "+":    
                    stack.append(operand2 + operand1)
                elif token == "-":
                    stack.append(operand2 - operand1)
                elif token == "*":
                    stack.append(operand2 * operand1)
                    print(stack)
                elif token == "/":
                    stack.append(operand2 / operand1)
        print(stack)
        return int(stack[0])