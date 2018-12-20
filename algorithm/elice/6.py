import sys

def kkongcha(arr, rabbit) :
    orderArr = []

    for i in range(len(arr)):
        order = [arr[i]]
        if rabbit == i:
            order.append(1)
        else:
            order.append(0)

        orderArr.append(order)

    orderArr = sorted(orderArr, key=lambda x:x[0], reverse=True)
    
    for order in range(len(orderArr)):
        if orderArr[order][1] == 1:
            return order+1


def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    loop = int(input())

    for i in range(loop):
        temp = [int(x) for x in input().split()]
        n = temp[0]
        rabbit = temp[1]

        orderCountArray = [int(x) for x in input().split()]

        print(kkongcha(orderCountArray, rabbit))

if __name__ == "__main__":
    main()
