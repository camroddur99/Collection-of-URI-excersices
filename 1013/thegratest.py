from sys import stdin

def main():
    arr = [int(x) for x in stdin.readline().split()]
    arr.sort()
    print(arr[2],"eh o maior")
main()
