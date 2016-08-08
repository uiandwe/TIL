#Python WSGI server

###먼저 웹서버란
인터넷을 통해서 요청된 웹 컨텐츠의 전달을 도와주는 하드웨어와 소프트웨어

### CGI(Common Gateway Interface)
웹서버는 static. 정적인 페이지만을 제공
사용자의 이벤트에 따라 원하는 페이지를 제공하기 위해서 프로그램 필요.
그리고 그 프로그램과 웹서버를 연결해주는 인터페이스가 CGI

###WSGI(Web Server Gateway Interface)
파이썬용 web application/framework 용 인터페이스(한마디로 파이썬용 CGI)
여러 wsgi가 존재 했지만 현재 대세는 uwsgi
