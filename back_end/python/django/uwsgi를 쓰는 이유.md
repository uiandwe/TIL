# uwsgi를 쓰는 이유

반드시 Nginx와 같이 써야 하는 것은 아니다. uWSGI 만으로도 Service를 제공하는 것이 가능하다. 


가능한가 가능하지 않은가에 답변에 대해서는 가능하다는 답변을 먼저 할 수 있다. 

그렇다면 Nginx와 같이 사용하므로서 얻는 이득은 무엇인가? 

가장 큰 장점중에 하나는 Nginx가 가진 보다 향상된 Static Content (CSS, Javascript 등) 
핸들링을 통해서 서버에 발생되는 Load를 줄일 수 있다.

- Static File Serving
- Reverse Proxy
- Caching
- Task Queuing

결국 nginx를 않써도 uwsgi만으로도 서비스가 가능하며, runserver는 단순이 웹서버 역활을 한다면
uwsgi는 캐싱 및 핸들링, load최적화로 인해 속도가 빨라짐
