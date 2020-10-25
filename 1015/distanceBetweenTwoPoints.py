from sys import stdin

def main():
    arr1 = stdin.readline().split()
    arr2 = stdin.readline().split()
    print("{:.4f}".format((((float(arr2[0])-float(arr1[0]))**2)+((float(arr2[1])-float(arr1[1]))**2))**(1/2)))        
main()
