sudo uwsgi --ini django.ini --protocol=http --socket 127.0.0.1:8000 --check-static /www/devblog_server --pidfile /tmp/blog.pid


fuser -n tcp -k 8000


uwsgi --stop /tmp/myapp.pid
kill `pidof uwsgi`
