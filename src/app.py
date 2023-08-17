from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)

    return json_text



@app.route('/todos', methods=['POST'])
def add_new_todo():
   
    # request_body = request.json
    request_body = request.get_json(force=True)
    todos.append(request_body)

    print("Incoming request with the following body", request_body, todos)
   
   
    return jsonify(todos) 


#"""DELETE"""#
@app.route('/todos/<int:position>', methods=['DELETE'])

def delete_todo(position):
     id == position
     todos.pop(position)
    
     print("This is the position to delete: ",position)
    
     return jsonify(todos)






# 
#     request_body = request.get_json(force=True) 
#     print("Incoming request with the following body", request_body)
   
   
#     return jsonify(todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)