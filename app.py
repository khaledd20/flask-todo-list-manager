from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
users = []
tasks = []

# Function to find user
def find_user(username):
    return next((user for user in users if user['username'] == username), None)

# Function to find task
def find_task(task_id):
    return next((task for task in tasks if task['id'] == task_id), None)

# User Registration
@app.route('/register', methods=['POST'])
def register():
    user = request.json
    if find_user(user['username']):
        return jsonify({"message": "User already exists"}), 400
    users.append(user)
    return jsonify({"message": "User registered successfully"}), 201

# User Login
@app.route('/login', methods=['POST'])
def login():
    user = request.json
    registered_user = find_user(user['username'])
    if registered_user and registered_user['password'] == user['password']:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

# CRUD Operations for Tasks
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    task['id'] = len(tasks) + 1
    tasks.append(task)
    return jsonify(task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = request.json
    existing_task = find_task(task_id)
    if existing_task:
        existing_task.update(task)
        return jsonify(existing_task), 200
    else:
        return jsonify({"message": "Task not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"message": "Task deleted"}), 200

# Search Functionality
@app.route('/tasks/search', methods=['GET'])
def search_tasks():
    query = request.args.get('q')
    filtered_tasks = [task for task in tasks if query.lower() in task['name'].lower()]
    return jsonify(filtered_tasks), 200

# Task Categorization
@app.route('/tasks/category/<string:category>', methods=['GET'])
def get_tasks_by_category(category):
    filtered_tasks = [task for task in tasks if task['category'].lower() == category.lower()]
    return jsonify(filtered_tasks), 200

# Task Prioritization
@app.route('/tasks/priority/<string:priority>', methods=['GET'])
def get_tasks_by_priority(priority):
    filtered_tasks = [task for task in tasks if task['priority'].lower() == priority.lower()]
    return jsonify(filtered_tasks), 200

if __name__ == '__main__':
    app.run(debug=True)
