#클로져 Closure

클로저는 독립적인 (자유) 변수를 가리키는 함수이다. 또는, 클로저 안에 정의된 함수는 만들어진 환경을 '기억한다'.

```
function init() {
  var name = "모질라"; // init에 있는 지역 변수 name
  function displayName() { // 내부 함수, 즉 클로저인 displayName()
    alert(name); // 부모 함수에 정의된 변수를 사용한다
  }
  displayName();
}
init();
```

함수 init()은 지역 변수 name과 함수 displayName()을 정의한다. 
displayName()은 함수 init() 안에 정의되어 그 함수(init()) 안에서만 사용할 수 있는 내부 함수이다. 
함수 displayName() 자신은 지역변수를 가지지 않지만 외부 함수에 정의된 변수에 접근하는 권한이 있어 부모 함수에 있는 변수 
name을 사용할 수 있다.


```
function makeFunc() {
  var name = "모질라";
  function displayName() {
    alert(name);
  }
  return displayName;
}

var myFunc = makeFunc();
myFunc();
```


이 코드를 실행하면 앞서 예로 들은 init() 함수와 동일한 결과를 보이는걸 알 수 있다(알람창에 "모질라" 문자열이 보일 것이다). 
위 예제와 다른 점, 그리고 흥미로운 점은 외부함수의 리턴 값이 내부함수 displayName() 라는 것이다


이 코드가 여전히 작동하는 것은 직관적이지 않다. 일반적으로 함수안에 정의된 지역변수는 함수가 실행하는 동안에만 존재한다.
makeFunc() 함수가 종료될 때 이 함수 내부에 정의된 지역변수는 없어지는게 상식적이다.
이 코드가 문제없이 동작하는 걸 보면 다른 일이 일어나고 있는 것 같다!

이것은 myFunc 함수가 클로저이기 때문이다. 클로저는 두 개의 것(함수, 그 함수가 만들어진 환경)으로 이루어진 특별한 객체의 한 
종류이다. 환경이라 함은 클로저가 생성될 때 그 범위 안에 있던 여러 지역 변수들로 이루어진다. 이 경우에 myFunc는 displayName 
함수와 "모질라" 문자열을 포함하는 클로저이다.


```
function makeAdder(x) {
  return function(y) {
    return x + y;
  };
}

var add5 = makeAdder(5);
var add10 = makeAdder(10);

print(add5(2));  // 7
print(add10(2)); // 12
```
여기서 인자 x를 받아 새 함수를 반환하는 makeAdder(x) 라고 하는 하나의 인자를 받는 함수를 만들었다. 반환되는 함수는 인자 y를
받아서 x 값과 y 값의 합을 돌려주는 함수이다.

본질적으로 makeAdder는 함수 공장(자신의 인자에 특정 값을 더하는 함수들을 만들어내는 것을 말한다)이다. 위의 예제에서 두개의 
함수를 찍어냈다. 첫째는 인자에 5를 더하는 함수이고 둘째는 인자에 10을 더하는 함수이다.

add5와 add10은 둘다 클로져이다. 두 함수는 같은 정의를 가지지만 다른 환경을 저장한다. add5의 환경에서 x는 5이지만 add10 의 
환경에서 x는 10이다.

```
var counter = (function() {
  var privateCounter = 0;
  function changeBy(val) {
    privateCounter += val;
  }
  return {
    increment: function() {
      changeBy(1);
    },
    decrement: function() {
      changeBy(-1);
    },
    value: function() {
      return privateCounter;
    }
  }   
})();

console.log(counter.value()); // logs 0
counter.increment();
counter.increment();
console.log(counter.value()); // logs 2
counter.decrement();
console.log(counter.value()); // logs 1
```

모듈 패턴이라고 알려진 클로저를 통해 몇 개의 public 함수가 private 함수와 변수에 접근하는 코드가 있다.
이전 예제에서는 각 클로저가 자기만의 환경을 가졌지만 이 예제에서는 하나의 환경을 counter.increment, counter.decrement, 
counter.value 세 함수가 공유한다.



https://developer.mozilla.org/ko/docs/Web/JavaScript/Guide/Closures
