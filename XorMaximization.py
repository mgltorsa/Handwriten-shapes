def Main():
    input()
    numbers=input().split(" ")
    print(int(numbers[0])^int(numbers[1])^int(numbers[2]))

def case(numbers):
    max=-1
    before=numbers[0]
    for n in range(1,len(numbers)):
        if numbers[n]>max:
            max=numbers[n]
            before=numbers[n]

    return max

Main()