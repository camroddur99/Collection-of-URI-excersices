from sys import stdin

def main():
    x,y = int(stdin.readline()),float(stdin.readline())
    print("{:.3f}".format(x/y),"km/l")
main()
