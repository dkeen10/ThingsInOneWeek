"""
2.1 Reverse Polish Notation
Difficulty: ★☆☆☆☆

An RPN calculator is a simple application of the stack data structure. 
When it comes to data structure, many folks will think of LeetCode. 
How about coding something that resembles a useful thing? There are also hardware RPN calculators which you can try to emulate.
"""

# Path: Calculator.py


def calculate(expression):
    """
    Evaluate an expression in Reverse Polish Notation.
    """
    stack = []
    for token in expression.split():
        if token == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif token == '-':
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        elif token == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif token == '/':
            a = stack.pop()
            b = stack.pop()
            stack.append(b / a)
        else:
            stack.append(int(token))
    return stack[0]



def main():
    """
    Main function.
    """
    while True:
        expression = input('> ')
        if expression == 'exit':
            break
        result = calculate(expression)
        print(result)

if __name__ == "__main__":
    main()  

