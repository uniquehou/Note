from tornado.web import RequestHandler
from Note.handler import BaseHandler
from .forms import *
from .models import *
import json


class AddHandler(BaseHandler):
    async def get(self, *args, **kwargs):
        self.render("add.html")

    async def post(self, *args, **kwargs):
        re_data = {}
        param = self.request.body_arguments
        form = NoteForm(param)
        if form.validate():
            note = await self.application.objects.create( Note, title=form.title.data, content=form.content.data)
            re_data['status'] = 1
            re_data['id'] = note.id
        else:
            for field in form.errors:
                re_data[field] = form.errors[field][0]
        self.finish(re_data)


class ListHandler(RequestHandler):
    async def get(self, *args, **kwargs):
        notes = await self.application.objects.execute( Note.select() )
        self.render("list.html", notes = notes)
