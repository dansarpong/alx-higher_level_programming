#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hide = dir(hidden_4)
    for name in hide:
        if name[:2] == "__":
            continue
        print("{}".format(name))
