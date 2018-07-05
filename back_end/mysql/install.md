```

$ sudo apt-get update

$ sudo apt-get install mysql-server

- 설치 (설치 중 root 암호 입력)


$ sudo mysql_secure_installation

- 보안 설정


$ sudo mysql_install_db

- 기본 디비 설치


$ mysql -u root -p

mysql> select version();

- mysql 버전 확인



* 외부 접근 허용

mysql> use mysql;

mysql> select host, user, password from user;

- 현재 접속 가능한 유저

1) 특정 IP 접근 허용 설정
mysql> grant all privileges on *.* to 'root'@'10.221.55.8' identified by 'root의 패스워드';

2) 특정 IP 대역 접근 허용 설정
mysql> grant all privileges on *.* to 'root'@'10.221.%' identified by 'root의 패스워드';

3) 모든 IP의 접근 허용 설정
mysql> grant all privileges on *.* to 'root'@'%' identified by 'root의 패스워드';


mysql> select host, user, password from user;
mysql> flush privileges;

mysql> exit


sudo vi /etc/my.cnf (혹은 sudo vi /etc/mysql/my.cnf)
- 아래부분 주석처리
# bind-address = 127.0.0.1


$ sudo /etc/init.d/mysqld restart

- mysql 재시작



```
