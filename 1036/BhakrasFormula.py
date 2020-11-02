from sys import stdin


def main():
    arr = [float(x) for x in stdin.readline().split()]
    possible = True
    poscal = (arr[1]**2)-(4*arr[0]*arr[2])
    if poscal < 0:
        print("Impossivel calcular")


main()
