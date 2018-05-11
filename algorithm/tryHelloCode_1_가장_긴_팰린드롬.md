```

앞뒤를 뒤집어도 똑같은 문자열을 palindrome이라고 합니다.
longest_palindrom함수는 문자열 s를 매개변수로 입력받습니다.
s의 부분문자열중 가장 긴 palindrom의 길이를 리턴하는 함수를 완성하세요.
예를들어 s가 "토마토맛토마토"이면 7을 리턴하고 "토마토맛있어"이면 3을 리턴합니다.


function longest_palindrom(str){
  var max_length = 1;
    for(var i=0; i<str.length; i++){
        for(var j=i; j<str.length; j++){
            var temp_str = str.substr(i, j+1);
            var reverse_str = temp_str.split("").reverse().join("");
            if(temp_str == reverse_str && temp_str.length > max_length){
                max_length = temp_str.length; 
            }
        }
    }

    return max_length;
}


// 아래는 테스트로 출력해 보기 위한 코드입니다.
console.log( longest_palindrom("토마토맛토마토") )
console.log( longest_palindrom("토마토맛있어") )


```
