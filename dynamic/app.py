from flask import Flask
from datetime import datetime
import subprocess
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def pull():
    path = os.path.dirname(__file__)
    os.chdir(path)
    output = subprocess.check_output('git pull', shell=True)
    s = 'pulled at {}'.format(datetime.now())
    s += '<pre>{}</pre>'.format(output)
    return s

if __name__ == '__main__':
    app.run(debug=True, listen=('', 6560))
