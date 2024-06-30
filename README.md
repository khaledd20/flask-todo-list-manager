# Flask To-Do List Manager

A simple To-Do List Manager application built with Flask, featuring user registration, login, CRUD operations for tasks, task categorization, task prioritization, and RESTful web services.

## Features

1. User Registration
2. User Login
3. CRUD operations for tasks (Create, Read, Update, Delete)
4. Task categorization
5. Task prioritization
6. RESTful web services for task management and user authentication

## Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/flask-todo-list-manager.git
    cd flask-todo-list-manager
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

### API Endpoints

- **Register a user**
    - `POST /register`
    - Request Body:
        ```json
        {
            "username": "yourusername",
            "password": "yourpassword"
        }
        ```

- **Login a user**
    - `POST /login`
    - Request Body:
        ```json
        {
            "username": "yourusername",
            "password": "yourpassword"
        }
        ```

- **Create a task**
    - `POST /tasks`
    - Request Body:
        ```json
        {
            "name": "Task name",
            "category": "Task category",
            "priority": "Task priority"
        }
        ```

- **Get all tasks**
    - `GET /tasks`

- **Update a task**
    - `PUT /tasks/<task_id>`
    - Request Body:
        ```json
        {
            "name": "Updated task name",
            "category": "Updated task category",
            "priority": "Updated task priority"
        }
        ```

- **Delete a task**
    - `DELETE /tasks/<task_id>`

- **Search tasks**
    - `GET /tasks/search?q=search_query`

- **Get tasks by category**
    - `GET /tasks/category/<category>`

- **Get tasks by priority**
    - `GET /tasks/priority/<priority>`

## License

This project is licensed under the MIT License.
