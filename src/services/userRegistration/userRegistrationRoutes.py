from flask import Flask, request, jsonify
from services.userRegistration.userRegistrationController import handle_registration, handle_login

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    password = data['password']
    if handle_registration( email, password):
        return jsonify({"message": "User registered successfully!"}), 201
    else:
        return jsonify({"message": "Registration failed!"}), 400

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    password = data['password']
    if handle_login(email, password):
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid credentials!"}), 401

if __name__ == '__main__':
    app.run(debug=True)
