import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    name_parts = name.split(" ")
    
    # Ensure the command is a flat list of strings
    if len(name_parts) > 1:
        command = name_parts
    else:
        command = [name]
    
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f'Error executing command: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
