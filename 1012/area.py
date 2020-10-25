from sys import stdin

def main():
    arr = [float(x) for x in stdin.readline().split()]
    print("TRIANGULO:,"{:.3f}".format((arr[0]*arr[2])/2))
    print("CIRCULO:","{:.3f}".format((3.14159)*(arr[2]**2)))
    print("TRAPEZIO:,"{:.3f}".format(((arr[1]+arr[0])*arr[2])/2))
    print("QUADRADO:","{:.3f}".format(arr[1]**2))
    print("RETANGULO:","{:.3f}".format(arr[0]*arr[1]))
main()
