

#call과 apply의 차이점은 무엇인가요?

apply와 call의 가장큰 차이점은 호출시 arguements를 전달하는 방법입니다.
apply는 배열형태로 전달하고 call은 쉼표로 구분해서 전달합니다.


아래와 같은 함수가 있을 때
```
var hello = function(name, age) {
      alert("제 이름은 " + name + "입니다." + "저는 " + age + "살 입니다.");
};
```


다음과 같이 호출할 수 있습니다.
```
hello("홍길동", 5); //일반적인 호출

hello.apply(undefined, ["홍길동", 5]); //apply를 사용한 호출

hello.call(undefined, "홍길동", 5); //call을 사용한 호출 
```
자세한 사항은 아래 내용을 참고하세요.

https://msdn.microsoft.com/library/4zc42wh1(v=vs.94).aspx

https://msdn.microsoft.com/ko-kr/library/7t96kt3h(v=vs.94).aspx


