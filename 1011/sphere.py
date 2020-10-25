from sys import stdin


def main():
    x = int(stdin.readline())
    value = (4/3)*(3.14159*(x**3))
    value = "{:.3f}".format(value)
    print("VOLUME =", value)


main()
