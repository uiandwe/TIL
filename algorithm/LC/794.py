
def backtrack(arr, ret, index):
    if index == len(arr):
        ret.append(''.join(arr))
    else:
        if arr[index].isalpha():
            arr[index] = arr[index].lower()
            backtrack(arr, ret, index+1)
            arr[index] = arr[index].upper()
            backtrack(arr, ret, index + 1)
        else:
            backtrack(arr, ret, index+1)


def solution(str):
    d = []
    array = list(str)
    backtrack(array, d, 0)
    print(d)


solution("a1b2")
