from sys import stdin

def main():
    x = int(stdin.readline())
    notes = [100,50,20,10,5,2,1]
    temp = x
    arr = []
    print(x)
    for i in range(len(notes)):
        arr.append(temp//notes[i])
        temp = temp%notes[i]
        print(arr[i],"nota(s) de R$",str(notes[i])+",00")
main()
