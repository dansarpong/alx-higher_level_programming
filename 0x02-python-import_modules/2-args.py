#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    num = len(argv) - 1
    if num == 0:
        end1, end2 = ("s", ".")
    elif num == 1:
        end1, end2 = ("", ":")
    else:
        end1, end2 = ("s", ":")

    print("{:d} argument{:s}{:s}".format(num, end1, end2))
    for i in range(1, num + 1):
        print("{:d}: {:s}".format(i, argv[i]))
