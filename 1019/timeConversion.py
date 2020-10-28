from sys import stdin


def main():
    x = int(stdin.readline())
    min = x // 60
    x = x % 60
    hor = min // 60
    min = min % 60
    print(str(hor)+":"+str(min)+":"+str(x))


main()
