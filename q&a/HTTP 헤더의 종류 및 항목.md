
#### http 메소드 형태
|method   |설명   | 
|---|---|---|---|---|
|GET   |요청받은 URI의 정보를 검색하여 응답   | 
|POST   |요청된 자원을 생성| 
|PUT   |전체 갱신|
|DELETE   |자원 삭제|
|HEAD   |웹서버 정보 확인, 헬스체크, 버전확인   |
|PATCH   |일부 갱신   |
|CONNECT   |프록시 기능 요청시 사용(ssl 터널용)   |
|TRACE   |테스트용   |
|OPTIONS   |지원되는 메소드 종류 확인   |

#### 응답코드
|응답대역   |코드   |  설명 | 
|---|---|---|---|---|
|성공   |200 | OK 응답 성공(GET)| 
|   |201 | Created 생성 성공(POST)| 
|   |204 | No content 전송할 데이터가 없는 성공(PUT/PATCH/DELETE)|
|리다이렉션   |301 | 변경된 타 URL에 요청함 / Redirect된 경우|
|클라이언트  요청에러   |400| Bad Request (사용자의 잘못된 요청)|
| |401 | Unauthorized (인증이 필요한 페이지를 요청) |
| | 403 | Forbidden (접근 금지) |
| | 404 | Not found, (요청한 페이지 없음)|
|서버에러   |500   | Internal server error (내부 서버 오류) |
|   |503 | Service unnailable (정기점검) |

