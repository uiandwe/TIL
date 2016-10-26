

server {
	listen 8080 ;

	root /www/devblog_server;
	index index.html index.htm;

	server_name blog.geeekdev.com;

	location / {
		proxy_pass http://127.0.0.1:8000;    
	}
}
