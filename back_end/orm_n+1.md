테이블 car, wheel 의 1:N의 관계가 있을시 

전체 car의  wheel을 가져올시 


<b>select * from  ( car join wheel )</b>


식의 쿼리가 될것이다. 


하지만 몇몇 orm에서는 

<b>select * from car where  = 1</b>

한 후 

<b>select * from wheel where car_id = 1</b>

<b>select * from wheel where car_id = 2</b>

<b>select * from wheel where car_id = 3</b>

<b>select * from wheel where car_id = 4</b>

....

식으로 N + 1로 검색 된다. 


이는 orm에서의 최적화 방법중 하나로 
만일 해당 데이터가 DB의 캐시 되지 않았을 경우 쿼리 도중 다시 가져오는 상황이 발생하게 된다. 
이를 미연에 방지 하고자 N+1과 같은 행동을 한다 ( 몇몇 상황에서는 join보다 더 빠른 결과 된다. ex- 캐시 되지 않은 메모리가 있을 경우 다시 메모리에 올려야 하므로 ) 


해결 방안

- Fetch Join 사용 (orm에서 지원하는 함수가 있을 경우에만)
- 글로벌 페치 전략 - LAZY 사용




https://stackoverflow.com/questions/97197/what-is-the-n1-selects-problem-in-orm-object-relational-mapping

https://meetup.toast.com/posts/87

https://jojoldu.tistory.com/165
