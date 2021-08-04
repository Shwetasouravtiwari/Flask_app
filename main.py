from flask import Flask, jsonify 
from flask_restful import Resource, Api , reqparse

app = Flask(__name__)
api= Api(app)

todos={
   1: {"task":"Program HelloWorld","summary":"use Python."},
   2: {"task":"Program 2","summary":"task2 in Python."},
   3: {"task":"Program 3","summary":"task3 in Python."}
}

class ToDoList(Resource):
    def get(self):
        return todos

class ToDo(Resource):
    def get(self,todo_id):
        return todos[todo_id]

"""class HelloWorld(Resource):
    def get(self):
        return{'data': 'Hello,World'}

class HelloName(Resource):
    def get(self,name):
        return{'data': 'Hello,{}'.format(name)}


api.add_resource(HelloWorld ,'/helloworld')
api.add_resource(HelloName ,'/helloworld/<string:name>')
"""
api.add_resource(ToDo ,'/todos/<int:todo_id>')
api.add_resource(ToDoList ,'/todos')
        
if __name__ == '__main__':
    app.run(debug=True)