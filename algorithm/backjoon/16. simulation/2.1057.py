num1 = input()
num2 = input()

forMax = max(num1, num2)
stage = 1


def checkOdd(a):
    if a % 2 != 0:
        return (a+1)/2
    else:
        return a/2


for i in range(forMax):
    stage += 1
    num1 = checkOdd(num1)
    num2 = checkOdd(num2)

    if num1+1 == num2 or num2+1 == num1:
        break


print stage
