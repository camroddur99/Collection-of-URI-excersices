from sys import stdin

def main():
    a, b, c = float(stdin.readline()), float(stdin.readline()), float (stdin.readline())
    oper = (a*2+b*3+c*5) / (2+3+5)
    oper = "{:.1f}".format(oper)
    print("MEDIA =",oper)
main()
