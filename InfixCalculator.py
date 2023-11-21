"""
2.2 Infix Operators
Difficulty: ★★☆☆☆

The difficulty increases with operator precedence. There are special algorithms to handle this, such as the shunting yard algorithm, which converts infix operators to RPN 
using 2 stacks.

Another way to do this is the recursive descent method from the JSON parser challenge. You can learn how this works by reading some open source compiler code.
"""

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


def toRPN(expression):
    """Evaluate an expression using infix operators by converting to RPN."""
    stack = []
    result = ''
    tokens = expression.split()
    for tok in tokens:
        if tok in ['*', '/']:
            while stack and stack[-1] in ['*', '/']:
                result += stack.pop() + ' '
            stack.append(tok)
        elif tok in ['+', '-']:
            while stack and stack[-1] != '(':
                result += stack.pop() + ' '
            stack.append(tok)
        elif tok == '(':
            stack.append(tok)
        elif tok == ')':
            while stack[-1] != '(':
                result += stack.pop() + ' '
            stack.pop()
        else:
            result += tok + ' '
    while stack:
        result += stack.pop() + ' '
    return result


def calculate(RPNexpression):
    stack = []
    tokens = stack.split()
    for tok in tokens:
        if tok not in operators:
            stack.append(float(tok))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(operators[tok](num2, num1))
    return stack.pop()


def main():
    """
    Main function.
    """
    while True:
        expression = input('> ')
        if expression == 'exit':
            break
        result = calculate(toRPN(expression))
        print(result)


if __name__ == "__main__":
    main()  
