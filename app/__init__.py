from flask import Flask, jsonify
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command("db", MigrateCommand)



from app.model.user_table import User
from app.model.autor import Autor
from app.model.post import Post
from app.model.comment import Comment

from app.controller import autor_controller
from app.controller import comment_controller

