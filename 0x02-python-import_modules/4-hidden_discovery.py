#!/usr/bin/python3
""" PYTHON """
if __name__ == "__main__":

    import hidden_4

    n = dir(hidden_4)

    for name in n:
        if not name.startswith("__"):
            print(name)
