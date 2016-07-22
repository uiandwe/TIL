#동일출처정책(the same-origin policy)

"동일출처정책(the same-origin policy)"은 한 출처(origin)에서 로드된 문서나 스크립트가 다른 출처 자원과
상호작용하지 못하도록 제약한다. 즉 이 정책 때문에  CORS 크로스 도메인 이슈 
(No 'Access-Control-Allow-Origin' header is present on the requested resource) 발생한다
그래서 jsonp를 쓰게 되고....


일반적인 브라우저는 프로토콜/포트/호스트가 다르면 정책이 발동하지만 IE는 포트가 달라도, 호스트가 최상위 호스트만 같다면 발동!!
(이러니...욕을..)

단 아래의 항목들은 제외(항상써오던 cdn과 기타 리소스들은 제외대상)
- ```<link rel="stylesheet" href="...">```을 사용한 CSS. CSS의 relaxed syntax rules 때문에, cross-origin CSS는 올바른 Content-Type 헤더가 필요하다. 제한은 브라우저에 따라 다르다: IE, Firefox, Chrome, Safari (CVE-2010-0051으로 스크롤 다운) 과 Opera.
- ```<img>``` 을 사용한 이미지. 지원되는 이미지 포맷은 다음을 포함한다 : PNG, JPEG, GIF, BMP, SVG, ...
- ```<video>``` 과 ```<audio>``` 를 사용한 미디어 파일.
- ```<object>```, ```<embed>``` 과 ```<applet>```을 사용한 플러그인.
- @font-face를 사용한 폰트. 몇몇 브라우저는 cross-origin 폰트를 허용하나, 그 외에는 동일 출처 폰트가 필요하다.
- ```<frame>``` 과 ```<iframe>```
