import json
from sqlite3 import IntegrityError
from app import app, db, Comment
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from datetime import datetime

@app.route("/comment/add", methods = ["POST"])
def comment_add():
    data = request.get_json()

    com = Comment(
        comentario = data["comentario"]
    )
    db.session.add(com)
    
    try:
        db.session.commit()
    
    except(IntegrityError):
        return jsonify({"error":True, "message": "ocorreu um erro" })
    
    return jsonify({"error":False, "message":"comentario criado com sucesso!"})


@app.route("/autor/edit/<id>", methods=["PUT"])
def autor_edit(id):
    data = request.get_json()
    com = Comment.query.get(id)

    if com is None:
        return jsonify({
            "message": "Não encontrado",
            "error": True
        }), 404

    com.nome = data["comentario"]
    try:
        db.session.commit()
    except(IntegrityError):
        return jsonify({"error": True, "message": "Ocorreu um erro ao EDITAR"})

    return jsonify ({"error": False, "message": "Editado com sucesso"})

    
@app.route("/comment/list", methods = ["GET"])
def comment_list():
    comentarios = Comment.query.all()
    output = {"data":[], "error":False}
    for comentario in comentarios:
        output["data"].append(comentario.to_dict())
    return jsonify(output)