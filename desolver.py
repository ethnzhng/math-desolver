import sys
import random


def factors(n):
    # Return a list of factors of n (excluding 1 and n)
    return [x for x in range(2, n) if n % x == 0]


def de_solve(n, depth):
    if n == 1 or n == 2:
        return str(n)
    # Prevent hanging on large numbers
    elif n > 1000000:
        return str(n)
    elif depth == 0:
        return str(n)
    else:
        # Randomly pick an operation
        operation = random.choice(['+', '-', '*', '/'])
        # Randomly pick one of the operands
        if operation in ['+', '-', '/']:
            operand = random.randint(2, n-1)
        elif operation == '*':
            factors_list = factors(n)
            if len(factors_list) == 0:
                # If no factors found, return original number
                return str(n)
            operand = random.choice(factors_list)

        if operation == '+':
            result = n - operand
            expression = (de_solve(operand, depth-1),
                          de_solve(result, depth-1), '+')
        elif operation == '-':
            result = n + operand
            expression = (de_solve(result, depth-1),
                          de_solve(operand, depth-1), '-')
        elif operation == '*':
            result = n // operand
            expression = (de_solve(operand, depth-1),
                          de_solve(result, depth-1), '*')
        elif operation == '/':
            result = n * operand
            expression = (de_solve(result, depth-1),
                          de_solve(operand, depth-1), '/')

        return expression


def to_standard(expression):
    if isinstance(expression, str):
        return expression
    elif isinstance(expression, tuple):
        left = to_standard(expression[0])
        right = to_standard(expression[1])
        operator = expression[2]
        return f"({left} {operator} {right})"
    else:
        return str(expression)


def to_latex(expression):
    if isinstance(expression, str):
        return expression
    elif isinstance(expression, tuple):
        left = to_latex(expression[0])
        right = to_latex(expression[1])
        operator = expression[2]
        if operator == '+':
            return f"({left} + {right})"
        elif operator == '-':
            return f"({left} - {right})"
        elif operator == '*':
            return f"{left} \\times {right}"
        elif operator == '/':
            return f"\\frac{{{to_latex(left)}}}{{{to_latex(right)}}}"
    else:
        return str(expression)


def main():
    if len(sys.argv) < 3:
        print("Usage: python desolver.py <number> <depth>")
        sys.exit(1)

    # Check that the arguments are integers
    try:
        n = int(sys.argv[1])
        depth = int(sys.argv[2])
    except ValueError:
        print("Error: Both arguments must be integers")
        sys.exit(1)

    n = int(sys.argv[1])
    depth = int(sys.argv[2])

    expression = de_solve(n, depth)

    standard = to_standard(expression)
    latex = to_latex(expression)

    # Verify that the expression is correct
    assert eval(standard) == n, "Expression does not evaluate to n"

    print(f"Standard Format:\n{standard}")
    print(f"\nLatex Format:\n{latex}")


if __name__ == '__main__':
    main()
