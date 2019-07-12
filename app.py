from flask import Flask, jsonify, request, render_template
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'haoshlf'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db' #location where the database is
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)

connect_db(app) #this is to connect app.py to the location that line9 tell where database is
db.create_all()

@app.route('/')
def show_cupcakes():
    return render_template("index.html")

@app.route('/cupcakes')
def show_all_cupcakes():
    """ make get request to show cupcakes """
    cupcakes_list = Cupcake.query.all()
    serialized_cupcakes = [
        {'flavor': cupcake.flavor, 
        'size': cupcake.size, 
        'rating': cupcake.rating, 
        'image': cupcake.image}
        for cupcake in cupcakes_list
    ]
    return jsonify(cupcakes=serialized_cupcakes)

@app.route('/cupcakes', methods=["POST"])
def post_cupcakes():
    response_cupcake = request.json
    cupcake = Cupcake(
        flavor=response_cupcake['flavor'],
        size=response_cupcake['size'],
        rating=response_cupcake['rating'],
        image=response_cupcake['image'] or None
    )

    db.session.add(cupcake)
    db.session.commit()

    serialized_cupcake = {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image
    }

    return jsonify(cupcake=serialized_cupcake)
    
@app.route('/cupcakes/<cupcake_id>', methods=["PATCH"])
def update_cupcakes(cupcake_id):

    cupcake = Cupcake.query.get(cupcake_id)

    response_cupcake = request.json
    cupcake.flavor = response_cupcake['flavor']
    cupcake.size = response_cupcake['size']
    cupcake.rating = response_cupcake['rating']
    cupcake.image = response_cupcake['image'] or "https://tinyurl.com/truffle-cupcake"

    db.session.commit()

    serialized_cupcake = {
        'id': cupcake.id,
        'flavor': cupcake.flavor,
        'size': cupcake.size,
        'rating': cupcake.rating,
        'image': cupcake.image
    }

    return jsonify(cupcake=serialized_cupcake)

@app.route('/cupcakes/<cupcake_id>', methods=["DELETE"])
def delete_cupcakes(cupcake_id):

    cupcake = Cupcake.query.get(cupcake_id)
    db.session.delete(cupcake)
    db.session.commit()

    return jsonify({"message": "delete"})

    