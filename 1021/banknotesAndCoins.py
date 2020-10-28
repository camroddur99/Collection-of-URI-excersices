from sys import stdin


def main():
    x = float(stdin.readline())
    notas = [100, 50, 20, 10, 5, 2]
    mon = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    print("NOTAS:")
    for i in range(len(notas)):
        print(str(int((x*100) // (notas[i]*100))) +
              " nota(s) de R$ " + str("{:.2f}".format(notas[i])))
        x = x % (notas[i])
    print("MOEDAS:")
    for i in range(len(notas)):
        print(str(int((x*100) // (mon[i]*100)))+" moeda(s) de R$ " +
              str("{:.2f}".format(mon[i])))
        x = x % (mon[i])


main()
