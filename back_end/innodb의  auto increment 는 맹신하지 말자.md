#innodb의  auto increment 는 맹신하지 말자.md

innodb의 auto increament는 파일 저장이 아닌 메모리 저장이다. 
즉 서버가 재가동 되는 순간 auto increament는 초기화가 되는것이다. 

만일 100번까지의 auto increament가 완료 되었고 다음번이 101번이 된다. 
이때 90번에 100까지의 데이터를 지웠다 다시 insert를 하면 101이 나온다.

but 90에서 100번까지 지우고 mysql를 재기동 하면 다음번 번호는 90번이 된다. 
해당 auto increament값으로 지정된 칼럼의 값을 검색해서 그 다음값으로 지정되는것이다. 



