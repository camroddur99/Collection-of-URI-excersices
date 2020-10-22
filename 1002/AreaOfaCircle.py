from sys import stdin

def main():
    r = float(stdin.readline())
    print("A="+str("{:.4f}".format(3.14159 * (r**2))))
main()
