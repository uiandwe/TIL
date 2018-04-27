

https://blog.naver.com/parkjy76/221262903257
- mysql 8.* 부터 오름차순 인덱스 공식 지원됨 



mysql에서는 order by에서의 desc(오름차순)은 인덱스가 지원하지 않는다. 

즉 order by desc를 할 경우 select된 데이터 들이 다시 sorting되므로 오버헤드가 발생한다. 

이를 막기 위해 

###숫자타입
- 숫자 타입은 반대 부호(음수는 양수로, 양수는 음수로) 변환해서 칼럼에 저장한다.
- 날짜 타입의 경우 타임스태프로 변환하여 음수로 저장한다. 
- select시 asc로 검색한다음 -를 곱해주면 원하는 값을 가져올수 있다.

```
select ( age * -1 ) as age from tb_member
order by age asc;
```

###문자 타입

- order by 가 1차일 경우엔 해당 쿼리를 asc로 가져온다음 for문을 반대로 돌린다. (디비서버가 다시 뒤집는 일을 for문으로 처리)
```
rs = exec("select name from tb_member order by name asc")

for( i = rs.index(); i>=0; i--){
       print(rs[i])
}
```

- order by 가 2차일 경우엔 해당하는 문자를 asc로 검색한 다음 해당 pk로 for문을 돌리며 다시 sql을 desc로 날린다. 

(전체 버퍼풀을 사용하지 않고 작은 작은 단위로 쪼개서 사용)

```
rs = exec("select name from tb_member group by name order by name asc")

while(rs.next()){
       print(exec("select * from tb_member where name="+rs.getString("name")+" order by region desc"))
}
```
