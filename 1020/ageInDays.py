from sys import stdin


def main():
    x = int(stdin.readline())
    an = x // 365
    x = x % 365
    mes = x // 30
    x = x % 30
    print(str(an)+" ano(s)")
    print(str(mes)+" mes(es)")
    print(str(x)+" dia(s)")


main()
