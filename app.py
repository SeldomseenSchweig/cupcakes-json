"""Flask app for Cupcakes"""
from crypt import methods
from flask import Flask, request, render_template, redirect, jsonify
from models import db, connect_db, Cupcake


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def list_of_cupcakes():
    cupcakes = Cupcake.query.all()
    return(render_template('index.html', cupcakes=cupcakes))


@app.route("/api/cupcakes")
def list_cupcakes():
    """GET route for all the cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]


    return jsonify({"cupcakes":all_cupcakes})


@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    """GET route for an individual cupcake"""
    cupcake = Cupcake.query.get_or_404(id).serialize()
    return jsonify({"cupcake":cupcake})


@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    new_cupcake=Cupcake(

        flavor=request.json["flavor"], 
        size=request.json["size"],
        rating=request.json["rating"],
        image=request.json["image"])

    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify({"cupcake":new_cupcake.serialize()})
    return (response_json, 201)




@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_Cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    # Cupcake.title = request.json.get("title", Cupcake.title)
    # Cupcake.done = request.json.get("done", Cupcake.done)
    db.session.query(Cupcake).filter_by(id=id).update(request.json)
    db.session.commit()
    jsonify_cupcake = jsonify(cupcake.serialize())
    return(jsonify_cupcake)


@app.route('/api/cupcakes/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="deleted")