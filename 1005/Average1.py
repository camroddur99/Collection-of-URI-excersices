from sys import stdin

def main():
    a, b = float(stdin.readline()), float(stdin.readline())
    oper = (a*3.5 + b*7.5)/(3.5+7.5)
    oper = "{:.5f}".format(oper)
    print("MEDIA =",oper)
main()
