from flask import Flask, jsonify, request
app = Flask(__name__)

# Endpoint to create and populate the database with dummy data
@app.route('/createdb', methods=['GET'])
def create_db():
    return jsonify({'message': 'Creates and populates the database with dummy data'})

# Home endpoint
@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'VAmPI home', 'Help': 'VAmPI is a vulnerable on-purpose API. It was created to evaluate the efficiency of third-party tools in identifying vulnerabilities in APIs but can also be used for learning/teaching purposes.'})

# Users endpoints
@app.route('/users/v1', methods=['GET'])
def get_all_users():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    return jsonify([{'email': 'user1@example.com', 'username': 'user1'}, {'email': 'user2@example.com', 'username': 'user2'}])

@app.route('/users/v1/_debug', methods=['GET'])
def debug_users():
    return jsonify([{'admin': True, 'email': 'user1@example.com', 'password': 'hashed_password', 'username': 'user1'},
                    {'admin': False, 'email': 'user2@example.com', 'password': 'hashed_password', 'username': 'user2'}])

@app.route('/users/v1/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    # Implement user registration logic
    return jsonify({'message': 'Successfully created user', 'status': 'success'})

# Add other user endpoints

# Books endpoints
@app.route('/books/v1', methods=['GET'])
def get_all_books():
    return jsonify({'Books': [{'book_title': 'Book1', 'user': 'user1'}, {'book_title': 'Book2', 'user': 'user2'}]})

# Add other book endpoints

if __name__ == '__main__':
    app.run(port=5000)
