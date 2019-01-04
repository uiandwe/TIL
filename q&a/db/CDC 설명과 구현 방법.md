## CDC 설명과 구현 방법

change data capture로 써 sql에서 실행된(커밋) 모든 쿼리 로그.


시간순으로 진행되며, 해당 진행에 따라 각각의 날짜별 데이터로의 복구가 가능하다.


mssql - cdc , mysql - binlog 로 확인 가능


프레임워크의 ORM 혹은 실행시킨 각각의 요청 쿼리를 commit; 을 날리는 순간 로그로 저장 (변경된 데이터만 저장하면 되므로 select는 제외)
