#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    argv = sys.argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if argv[1] not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[0])
    b = int(argv[2])
    result = operators[argv[1]](a, b)
    print("{} {} {} = {}".format(a, argv[1], b, result))
