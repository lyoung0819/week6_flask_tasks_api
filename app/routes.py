from app import app 
from all_tasks.tasks import tasks_list
from flask import request


@app.route('/')
def index():
    return f'this is the index page'

@app.route('/tasks')
def get_all_tasks():
    tasks = tasks_list
    return tasks

@app.route('/tasks/<int:task_id>')
def get_task_by_id(task_id):
    tasks = tasks_list
    for task in tasks:
        if task['id'] == task_id:
            return task
    return {'error': f'A task with the ID of {task_id} does not exist'}, 404 

#Create route to create new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Check to make sure the request object body is JSON
    if not request.is_json:
        return {'error': 'your content-type must be application/json'}, 400
    # Get data from request body 
    data = request.json 
    # Want to set it up where each task must have a title & body 
    # Valide the incoming data - first write out required fields, and check against it
    required_fields = ['title', 'description', 'dueDate']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400

    # Get data values
    title = data.get('title')
    description = data.get('description')
    dueDate = data.get('dueDate')


    # Create new task dictionary 
    new_task = {
        'id' : len(tasks_list) + 1,
        'title' : title,
        'description' : description,
        'dueDate': dueDate, 
        'completed': bool,
        'createdAd': '2024-03-29T15:23:11'
    }

    # Add the new post to storage (new_task)
    tasks_list.append(new_task)

    # Return the newly created task dictionary with a 201 Created Status Code
    return tasks_list, 201