from tornado import web
import tornado.ioloop
from Note.urls import urlpattern
from Note.settings import settings
import peewee_async

if __name__ == "__main__":
    app = web.Application(urlpattern, debug=True, **settings)
    app.listen(8888)

    database = peewee_async.MySQLDatabase(**settings['db'])
    app.objects = peewee_async.Manager(database)  # 之后通过此协程的商品对数据库操作
    database.set_allow_sync(False)

    tornado.ioloop.IOLoop.current().start()
