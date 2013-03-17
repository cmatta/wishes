from flask import Flask
from flask_peewee.db import Database
from flask_peewee.auth import Auth
from flask_peewee.admin import Admin, ModelAdmin
from flask_peewee.rest import RestAPI
from peewee import *

DATABASE = {'name': 'wishes.db',
            'engine': 'peewee.SqliteDatabase'}

DEBUG = True
SECRET_KEY = "phoenixx"

app = Flask(__name__)
app.config.from_object(__name__)

db = Database(app)

class Wish(db.Model):
  HitId = CharField()
  HitTitle = CharField()
  Annotation = CharField(null=True)
  AssignmentId = CharField()
  WorkerId = CharField()
  Status = CharField()
  AcceptTime = DateTimeField()
  SubmitTime = DateTimeField()
  Wish = CharField()

class WishAdmin(ModelAdmin):
  columns = ('Wish', 'WorkerId', 'SubmitTime')

auth = Auth(app, db)
admin = Admin(app, auth)
api = RestAPI(app)

api.register(Wish)
admin.register(Wish, WishAdmin)

api.setup()
admin.setup()


@app.route("/")
def index():
  return "Hello World"


if __name__ == '__main__':
  auth.User.create_table(fail_silently=True)
  Wish.create_table(fail_silently=True)

  app.run()