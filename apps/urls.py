from tornado.web import url
from .handler import *

urlpattern = [
    url("/add/", AddHandler),
    url("/list/", ListHandler),
]