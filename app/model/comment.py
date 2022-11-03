from requests import post
from app import db
from sqlalchemy import Column
from app.model.autor import Autor



class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    comentario = db.Column(db.Text, nullable = False)
    
    
    def __init__(self, comentario):      
        self.comentario = comentario
        
    def __repr__(self):
        str = "<Comenta {} {}>".format(self.id, self.comentario)
        return str

    def to_dict(self):
        return {
            "id": self.id,
            "comentario": self.comentario
        }
