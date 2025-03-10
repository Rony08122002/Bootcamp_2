from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
import openai

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wedding.db'  # ניתן לשנות ל-PostgreSQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    
class Wedding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    couple_name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.Float, nullable=False)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wedding_id = db.Column(db.Integer, db.ForeignKey('wedding.id'), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(255))
    price_range = db.Column(db.String(100))

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wedding_id = db.Column(db.Integer, db.ForeignKey('wedding.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    rsvp_status = db.Column(db.String(50), default='Pending')

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat_page():
    return render_template('chat.html')

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    new_expense = Expense(wedding_id=data['wedding_id'], category=data['category'], amount=data['amount'], description=data.get('description', ''))
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({"message": "Expense added successfully"})

@app.route('/add_vendor', methods=['POST'])
def add_vendor():
    data = request.json
    new_vendor = Vendor(name=data['name'], category=data['category'], contact_info=data.get('contact_info', ''), price_range=data.get('price_range', ''))
    db.session.add(new_vendor)
    db.session.commit()
    return jsonify({"message": "Vendor added successfully"})

@app.route('/add_guest', methods=['POST'])
def add_guest():
    data = request.json
    new_guest = Guest(wedding_id=data['wedding_id'], name=data['name'], rsvp_status=data.get('rsvp_status', 'Pending'))
    db.session.add(new_guest)
    db.session.commit()
    return jsonify({"message": "Guest added successfully"})

@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_message = data.get('message', '')
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )
    
    reply = response["choices"][0]["message"]["content"]
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
