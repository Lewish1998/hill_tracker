from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/hills_db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://@localhost/hills_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Hills(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.VARCHAR(255), nullable=False)
    description = db.Column(db.VARCHAR(255))
    distance_km = db.Column(db.DECIMAL)
    ascent_metres = db.Column(db.INTEGER)
    difficulty = db.Column(db.INTEGER)
    latitude = db.Column(db.DECIMAL)
    longitude = db.Column(db.DECIMAL)
    favourite = db.Column(db.BOOLEAN)
    time_added = db.Column(db.TIMESTAMP, server_default=db.func.now(), nullable=False)
    
class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    firstname = db.Column(db.VARCHAR(255), nullable=False)
    lastname = db.Column(db.VARCHAR(255), nullable=False)
    email = db.Column(db.VARCHAR(255), nullable=False)
    email_update = db.Column(db.BOOLEAN, nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)
    time_added = db.Column(db.TIMESTAMP, server_default=db.func.now(), nullable=False)
    
class FavouriteHills(db.Model):
    user_id = db.Column(db.INTEGER, db.ForeignKey('users.id'), primary_key=True)
    hills_id = db.Column(db.INTEGER, db.ForeignKey('hills.id'), primary_key=True)
    time_added = db.Column(db.TIMESTAMP, server_default=db.func.now())


# with app.app_context():
#     db.create_all()
    
@app.route('/')
def index():
    hills = Hills.query.all()
    users = Users.query.all()
    # favs = FavouriteHills.query.all()
    return render_template('index.html', hills=hills, users=users)

@app.route('/hills')
def get_hills():
    hills = Hills.query.all()
    hills_list = []
    for hill in hills:
        hills_list.append({
            'id': hill.id,
            'name': hill.name,
            'description': hill.description,
            'distance_km': float(hill.distance_km),
            'ascent_metres': hill.ascent_metres,
            'difficulty': hill.difficulty,
            'latitude': float(hill.latitude),
            'longitude': float(hill.longitude),
            'favourite': hill.favourite,
            'time_added': hill.time_added.isoformat()
        })
    return jsonify(hills_list)

@app.route('/hills', methods=["POST"])
def create_hill():
    data = request.json
    new_hill = Hills(
        name=data['name'],
        description=data['description'],
        distance_km=data['distance_km'],
        ascent_metres=data['ascent_metres'],
        difficulty=data['difficulty'],
        latitude=data['latitude'],
        longitude=data['longitude'],
        favourite=False,
    )
    db.session.add(new_hill)
    db.session.commit()
    return jsonify({'message': 'Hill created successfully'}), 201

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = Users(
        firstname=data['firstname'],
        lastname=data['lastname'],
        email=data['email'],
        password=data['password'],
        email_update=data['emailUpdate']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/users/login', methods=['POST'])
def login():
    data=request.json
    email=data['email']
    password=data['password']
    
    user = Users.query.filter_by(email=email).first()
    
    if user and user.password == password:
        return jsonify({'message': 'Login successful', 'user_id': user.id}), 200
    else:
        return jsonify({'error': 'Invalid email or password'}), 401


if __name__ == '__main__':
    app.run(debug=True)
    