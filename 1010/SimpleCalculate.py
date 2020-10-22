from sys import stdin

def main():
    arr1 = stdin.readline().split(" ")
    arr2 = stdin.readline().split(" ")
    oper = "{:.2f}".format(int(arr1[1])*float(arr1[2]) + int(arr2[1])*float(arr2[2]))
    print("VALOR A PAGAR: R$",oper)
main()
