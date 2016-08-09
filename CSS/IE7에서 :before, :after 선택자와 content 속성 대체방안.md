IE7을 고려해야하는 페이지를 제작하는 경우, :before 나 :after 와 같은 가상 선택자를 지원하지 않아 애를 먹곤 합니다. 

설상가상으로 content 속성까지 지원하지 않지요.

##:before, :after 선택자 대체방안

IE7에서는 :before 와 :after 가상 선택자를 대체하기 위해서 새로운 요소를 생성하고 이에 클래스명을 부여하는 방법이 사용된다. 
아래의 예시와 같이, 이 표현식은 자바스크립트와 같은 방식으로 요소를 생성하고 있다.

```
.example:before,
.example .ie-before {
    display: block;
    width: 100px;
    height: 50px;
}

.example {	
    *zoom: expression(
        this.runtimeStyle['zoom'] = '1', 
        this.insertBefore(document.createElement("i"), 
        this.firstChild).className="ie-before"
    );
}
```

content 속성 대체방안

IE7에서는 또한, CSS의 content 속성도 지원하지 않는다. 이는 가상 선택자들과 함께 자주 사용되는 속성이기에 이를 대체하는 방법
또한 알아본다. 위에서 사용한 IE 전용 표현식에 단순히 명령어를 추가하는 수준에서 이루어진다.

```
.love {
    *zoom: expression(
        this.runtimeStyle['zoom'] = '1',
        this.innerHTML = 'LOVE'
    );
}
```
