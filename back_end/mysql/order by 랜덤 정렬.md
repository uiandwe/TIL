```
select * from tb_member
order by rand()
limit 1;
```

위의 쿼리는 임의의 1건의 레코드를 가져오는 쿼리이다. 단 해당 테이블을 모두 읽은뒤 그중에 하나를 가져오므로 심각한 오버헤드가 발생한다. 

이에 테이블에 insert시 rand_val 칼럼에 랜덤한 값을 넣어주며 해당 칼럼을 인덱스를 추가한다.


```
insert into tb_member (member_id, rand_val) values ( nul, floor((rand()*10000000)));

백만 자리 랜덤으로 넣는 경우 예
```

그 다음 해당 rand_val로 검색하면 인덱스를 통한 검색으로 속도가 향상된다.

```
select * from tb_member
where rand_val >= floor((rand()*10000000))
order by rand_val asc limit 1;
```

