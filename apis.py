from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for testing
users_data = [
    {"email": "user1@example.com", "username": "user1"},
    {"email": "user2@example.com", "username": "user2"},
    # Add more users as needed
]

books_data = [
    {"book_title": "Book1", "owner": "user1", "secret": "Secret1"},
    {"book_title": "Book2", "owner": "user2", "secret": "Secret2"},
    # Add more books as needed
]

# /createdb
@app.route('/createdb', methods=['GET'])
def create_db():
    # Dummy implementation
    return jsonify({"message": "Creates and populates the database with dummy data"})

# /
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "VAmPI home", "Help": "Your help information here"})

# /users/v1
@app.route('/users/v1', methods=['GET'])
def get_all_users():
    return jsonify(users_data)

# /users/v1/_debug
@app.route('/users/v1/_debug', methods=['GET'])
def debug_users():
    return jsonify(users_data)

# /users/v1/register
@app.route('/users/v1/register', methods=['POST'])
def register_user():
    # Dummy implementation
    return jsonify({"message": "Successfully created user", "status": "success"})

# Add more routes for the remaining paths based on your needs

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
