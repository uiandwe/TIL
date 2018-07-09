
```

mysql 5.7 이상일 

1. index 추가

ex) ALTER TABLE 테이블명 ADD FULLTEXT INDEX 인덱스명 (컬럼명);
mysql > ALTER TABLE AppPurchases ADD FULLTEXT INDEX idx_message (message);

2. 검색
ex) SELECT * FROM 테이블명
WHERE MATCH(컬럼명) AGAINST('검색어1 검색어2')

mysql> SELECT * FROM AppPurchases WHERE MATCH(message) AGAINST('축하해')

3. 두글자일 경우 my.cnf 수정
innodb_ft_min_token_size=2

ft_min_word_len=2
```
