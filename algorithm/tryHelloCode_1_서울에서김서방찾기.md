```

findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하세요.
seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.




function findKim(seoul){
  var idx = 0;
  idx = seoul.indexOf("Kim");

  return "김서방은 " + idx + "에 있다";
}

// 실행을 위한 테스트코드입니다.
console.log( findKim(["Queen", "Tod", "Kim"]));


```
