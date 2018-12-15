from peewee import *
from datetime import datetime
from Note.settings import settings

class Note(Model):
    title = CharField(verbose_name="标题", max_length=100, index=True)
    content = CharField(verbose_name="内容", max_length=2000, default="", null=True)
    add_time = DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        database = MySQLDatabase(**settings['db'])