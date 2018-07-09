### mysql replication

```


master / slave 서버에 각각의 실행이 다르므로 주의할것!!

1. 설정 추가 

my.cnf 에 추가 (master)
[mysqld]
server-id = 1
log-bin = mysql-bin

mysql 재시작 
$ sudo /etc/init.d/mysql restart

my.cnf 에 추가 (slave)
[mysqld]
server-id = 2
log-bin = mysql-bin

mysql 재시작 
$ sudo /etc/init.d/mysql restart



2. 계정 추가 

master에 replication을 수행할 유저 추가 
(master mysql)
mysql > GRANT REPLICATION SLAVE ON *.* TO 'repl'@'192.168.100.0/ 255.255.255.0' IDENTIFIED BY '비번';


2-1. 덤프 (필요할 경우에만)
!! 수행하려는 master가 이미 테이블 및 데이터가 수정이 되었다면 덤프를 통해 slave를 동기화를 해줘야 한다. (아니면 그동안의 동기화가 깨져 에러가 난다.)

master 덤프
(master 콘솔)
$ mysqldump -u root -p --all-databases > dump.db

slave 에 추가 
(slave 콘솔)
$ mysql -u root -p < dump.db


3. slave에 마스터 정보 추가 

먼저 master_log_file / master_log_pos 의 정보는 master에서 정보 획득 
(master mysql)
mysql > show master status;


slave에 master 정보 추가
(slave mysql)
mysql > CHANGE MASTER TO MASTER_HOST='10.211.55.13',MASTER_USER='repl',MASTER_PASSWORD='비번', MASTER_LOG_FILE = 'mysql-bin.000001', MASTER_LOG_POS = 730 MASTER_PORT=3306, MASTER_CONNECT_RETRY=30;

4. 실행
slave replication 실행 
(slave mysql)
mysql > start slave;

!! 에러 확인
(slave msyql)
mysql > show slave status;
last_error 칼럼을 통해서 에러를 확인한다. 
```
