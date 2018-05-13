
```



function numberOfPrime(num) {
    var i = 2; // i : 나눌 대상
    var isPrime = true;
    var array = [];

    while (i <= num) {
        isPrime = true;
        for (var n = 2; n < i; n++) {
            if (i % n == 0) {
                isPrime = false;
            }
            continue;
        }

        if (isPrime == true)
            array.push(i);

        i++;
    }

    return array.length
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( numberOfPrime(10) )



```
