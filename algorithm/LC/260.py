def solution(array):
    xor = 0
    for i in array:
        xor ^= i

    idx = 0
    # 남은 두개의 서로 다른 비트값을 알아냄 (같은 숫자가 아니므로 한자리는 다름)
    for i in range(32):
        if ( xor >> i ) & 1 == 1:
            idx = i
            break

    print(xor, idx, bin(5) , bin(3))
    xor1 = 0
    xor2 = 0
    # 모든 숫자를 위에서 구한 자리가 다른 해당 자리가 1인것과 0인것으로 다 xor를 하면 
    # 같은 숫자들은 없어지므로, 서로 다른 숫자만 남게됨
    for i in array:
        if (i >> idx) & 1 == 1:
            xor1 ^= i
        else:
            xor2 ^= i

    print(xor1, xor2)

print(solution([3, 5, 6, 7, 6, 7]))
