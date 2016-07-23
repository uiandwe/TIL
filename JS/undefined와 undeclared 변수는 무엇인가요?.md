Javascript는 undefined 라는 특별한 형태가 존재한다. 

모든것이 object 로 통하는 javascript 에서의 null 은 값이 아닌 객체 참조의 연결을 해지하는 것을 말한다. 즉 어떤 참조값이 존재 
하지 않음으로 비어있는 값을 가진 변수가 되는 것이다.

undefined 는 선언만 되어지고 특정 값이 할당되지 않는 경우 javascript 엔진에 의해 자동으로 할당되는 값이다. 특별히 할당된 값이 
없는경우 일반적인 언어처럼 null 이 아니고 undefiend 가 할당 되는 것이다.

또한 객체가 소유하지 않은 프로퍼티에 접근하게 될 경우에도 undefined 가 반환된다.

undeclared 변수란 선언하지 않고도 사용가능한 변수라고 한다. 하지만 정확히는 이는 javascript 의 scope 개념에서 따져보면 
유효범위를 지정하지 않은 변수다.

javascript는 none typed 언어로서 var 라는 키워드를 사용하여 변수를 사용하는게 보편적으로 알려져 있는 사실이다.

하지만 이 var 키워드는 선언을 위한 키워드가 아니고 해당 변수의 유효범위를 지정하는 역활을 한다. 해당 키워드를 지정하지 않은 
변수는 global scope 에 저장 된다. 하지만 여기에는 한가지 제약사항이 따른다.

var 키워드 없이 사용된 변수는 할당문을 만나기전에 해당 변수에 참조를 만나면 오류를 내뱉게 된다.

```javascript
foo = 1;
console.log(foo+2);
>3

console.log(foo+2);
foo=1;
> Uncaught ReferenceError: foo is not defined

```




http://insanehong.kr/post/front-end-developer-interview-javascript/
