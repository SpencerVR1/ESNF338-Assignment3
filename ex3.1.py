import sys

# Define a stack class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

# Define a function to evaluate a prefix expression
def evaluate_expression(expression):
    stack = Stack()
    tokens = expression.split()

    # Iterate over the tokens in reverse order
    for token in reversed(tokens):
        token = token.replace("(", "")
        token = token.replace(")", "")
        if token.isdigit():
            stack.push(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Apply the operator to the operands
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2

            # Push the result onto the stack
            stack.push(result)

    # The final result will be at the top of the stack
    return stack.pop()

# Get the expression from the command line argument
expression = sys.argv[1]

# Evaluate the expression and print the result
result = evaluate_expression(expression)
print(result)
