#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    av = sys.argv
    op = "+", "*", "/", "-"
    if len(av) is not 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif av[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        op = av[2]
        a = int(av[1])
        b = int(av[3])
        if op == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif op == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif op == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
        elif op == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
