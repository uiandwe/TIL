#js 모듈 패턴


```
var namespace = (function(namespace, $, undefined){
// $ = jQuery임 전역번수를 지역변수로 전달하면 실행함수내에서 지역변수로 사용하기때문에 탐색작업이 좀더 빨라진다
    var i  = 0;
 
    function func1(){ //내부 함수 private
        alert(i);      
    };
    namespace.func2 = function(){ //외부 노출 함수 public
        alert(i);      
    };
   
    return namespace; //리턴을 해야함 
})(window.namespace || {},jQuery); //객체 없으면 생성
 
```
