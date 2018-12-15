from wtforms_tornado import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class NoteForm(Form):
    title = StringField("标题", validators=[DataRequired("请输入标题")])
    content = StringField("内容", validators=[DataRequired("请输入内容")])