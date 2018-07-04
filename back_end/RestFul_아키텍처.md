
#### REST

REpretational State Tarnsfer 의 약자로 직역하면 표면 상태 전송. 전송하는 과정에서 해당 상태를 표기하는 상태를 말한다. 
restful은 rest의 형태를 지킬 경우 restful하다 라고 말한다. 

#### RestFul

단순히 하나의 웹 페이지 클라이언트를 위해 하나의 서버를 구성한다면 모바일 기기와 다양한 웹 화면을 보여주기 위해 새로운 API를 개발해야 했습니다. 이 비효율적인 일을 방지 하기 위해 하나의 서버로 여러대의 클라이언트에 대응하도록 하며 해당 URI 만으로도 화면상의 리소스를 정의 할 수 있도록 표현하며 모든 리소스는 구조적이고 유기적으로 연결되어 있도록 설계하는 것이 RestFul 아키텍쳐 입니다.

먼저 RestFul 아키텍쳐를 사용하기 위한 몇가지 조건이 있습니다.

1. 공백 없이 하이픈 ( - , _ )을 사용하며 확장자를 사용하지 말것

- 공백이 들어갈 경우 %20과 같이 공백을 나타내기 위해 아스키코드가 들어가 데이터가 변형될수 있습니다.

- 파일은 header의 media type으로 구분합니다.

2. CRUD를 URI에 사용하지 말것

CRUD는 데이터의 처리 방식으로 Create(생성), Read(읽기), Update(갱신), Delete(삭제)의 앞글자들을 따서 만든 말입니다.

디비와 Rest api에서는 각각 다음과 같이 대응됩니다.
```
단어          sql         Rest api
Create      Insert      Post
Read        select      Get
Update      Update      Put/Patch
Delete      Delete      Delete
```

artist라는 객체를 표현한다면 URI형식은 /artists 복수형으로 시작하며 각 행동은 http method에 따라 화면과 액션이 달라지게 된다.
```
HTTP Verb 	    Path 	              action
GET 	          /artists 	          모든 아티스트 출력
GET 	          /artists/new 	      아티스트 입력 폼 출력
POST 	          /artists      	    아티스트 생성
GET 	          /artists/:id 	      해당 아티스트 출력
GET 	          /artists/:id/edit 	해당 아티스트 수정 폼 출력
PUT 	          /artists/:id 	      해당 아티스트 수정
DELETE 	        /artists/:id 	      해당 아티스트 삭제 
```
