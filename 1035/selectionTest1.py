from sys import stdin


def main():
    arr = [int(x) for x in stdin.readline().split()]
    x = "Valores nao aceitos"
    x1 = "Valores aceitos"
    if arr[0] % 2 == 0:
        if (arr[3] and arr[2]) > 0:
            if arr[2] + arr[3] > arr[0] + arr[1]:
                if arr[1] > arr[2] and arr[3] > arr[0]:
                    print(x1)
                else:
                    print(x)
            else:
                print(x)
        else:
            print(x)
    else:
        print(x)


main()
