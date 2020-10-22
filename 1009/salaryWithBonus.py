from sys import stdin

def main():
    name = stdin.readline()
    a,b = float(stdin.readline()),float(stdin.readline())
    oper = (a+(b*0.15))
    print("TOTAL = R$","{:.2f}".format(oper))
main()
