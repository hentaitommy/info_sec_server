uwsgi --ini /root/workDir/info_sec/info_sec_server/uwsgi.ini
启动uwsgi
killall -9 uwsgi
强制关闭uwsgi

/usr/local/nginx/sbin/nginx -s reload
#Nginx平滑重启方法

source /data/env/djangoenv/bin/activate
python进虚拟环境

python manage.py runserver
python manage.py runserver 0.0.0.0:8000