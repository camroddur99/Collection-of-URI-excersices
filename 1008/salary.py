from sys import stdin

def main():
    a,b = int(stdin.readline()),int(stdin.readline())
    c = float(stdin.readline())
    print("NUMBER =",a)
    oper = "{:.2f}".format((b*c))
    print("SALARY = U$",oper)
main()
