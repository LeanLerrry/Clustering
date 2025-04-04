workers = 4
threads = 2
bind = "0.0.0.0:10000"
worker_class = "gthread"
timeout = 300
wsgi_app = "wsgi:app"
