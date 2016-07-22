#호이스팅

호이스팅이란 무엇일까요? Hoisting이라는 단어를 직역하면 끌어올리기, 들어 올려 나르기라는 뜻입니다. 
JavaScript에서 호이스팅도 비슷한 의미를 갖고 있습니다. 간단하게 말해서 JavaScript에서의 호이스팅의 의미는 변수 선언문을 
끌어올린다는 뜻으로 이해하면 됩니다.

```javascirpt
function hoistingExam(){
    console.log("value="+value);
    var value =10;
    console.log("value="+value);
}
hoistingExam();
 
//실행결과
/*
value= undefined
value= 10
*/
```
의 호이스팅에 의해 아래와 같이 변환 됩니다.
```javascirpt
function hoistingExam(){
    var value;
    console.log("value="+value);
    value =10;
    console.log("value="+value);
}
hoistingExam();
//실행결과
/*
value= undefined
value= 10
*/
```

```javascirpt
var value=30;
function hoistingExam(){
    console.log("value="+value); 
    var value =10; 
    console.log("value="+value); 
}
hoistingExam(); 
//실행결과 
/* 
value= undefined 
value= 10
*/
```
그렇다면 위와 같은 코드에서는 어떤 결과가 나올까요? 다른 프로그래밍 언어에 익숙한 개발자 분들은 변수 value의 첫 호출에서 
전역변수가 참조된다고 생각하실 수 있습니다. 하지만 JavaScript의 호이스팅으로 인해서 선언 부가 함수 hoistingExam의 최상단에서
끌어올려 짐으로써 전역변수가 아닌 지역변수를 참조합니다.

