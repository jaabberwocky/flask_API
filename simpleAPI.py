from flask import Flask, jsonify, abort, make_response, request, g
from flask_httpauth import HTTPBasicAuth
from config_vars import test_username, test_password, DATABASE
import sqlite3

app = Flask(__name__)
auth = HTTPBasicAuth()

## authentication
@auth.get_password
def get_password(username):
    if username == test_username:
        return test_password
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

## db connections
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

## api routes
@app.route('/hello', methods=['GET'])
def index():
    # parse the GET request to see if name is in the params
    if "name" in request.args:
        # returns the name
        return "<h1>Hello {name}!</h1>".format(name=str(request.args['name']).title())
    else:
        return "<h1>Hello World!</h1>"

# returns ALL tasks
@app.route('/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    tasks = []
    for task in query_db('SELECT * FROM tasks'):
        tasks.append({
            'id':task[0],
            'name':task[1],
            'description':task[2],
            'status':task[3]
            })
    return jsonify(tasks=tasks)

# returns SPECIFIC tasks
@app.route('/tasks/<int:task_id>', methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = query_db('SELECT * FROM tasks WHERE ID = {id}'.format(id=task_id))
    if len(task) == 0:
        abort(404)
    else:
        return jsonify(
            id = task[0][0],
            name = task[0][1],
            description = task[0][2],
            status = task[0][3])

# updates SPECIFIC task
#@app.route('/tasks/insert', methods=['POST'])
#@auth.login_required
#def insert_task():
#    if not request.json or not "id" in request.json or not "name" in request.json or not "description" in request.json:
#        abort(400)
#    else:


if __name__ == '__main__':
    app.run(debug=True)