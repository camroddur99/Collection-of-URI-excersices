from sys import stdin

def main():
    x, y = int(stdin.readline()),int(stdin.readline())
    print("{:.3f}".format((x*y)/12))
main()
