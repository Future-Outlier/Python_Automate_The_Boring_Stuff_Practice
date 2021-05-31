import sys
def collatz(num): # input a integer
    while True:
        print(int(num))
        if num == 1:
            break
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = num * 3 + 1


num = input()
num = int(num)
collatz(num)

