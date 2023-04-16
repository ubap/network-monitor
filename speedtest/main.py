import subprocess
import json

output = json.loads(subprocess.check_output(['./speedtest', '--format=json-pretty']))

print(output)
