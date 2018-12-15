import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = {
    "static_path": "static",
    "static_url_prefix": "/static/",
    "template_path": "templates",
    # "secret_key": "iZdNU4UktK$zXzCq",
    # "jwt_expire": 7*24*3600,
    # "MEDIA_ROOT": os.path.join(BASE_DIR, "media"),
    # "SITE_URL": "http://127.0.0.1:8888",
    "db": {
        "database": "note",
        "host": "123.207.254.239",
        "port": 3306,
        "user": "win7",
        "password": "mysqlwin7pndc",
    },
    "redis": {
        "host": "127.0.0.1"
    }
}