from flask import Flask
from datetime import datetime
import subprocess
import os

app = Flask(__name__)
app.debug = True

@app.route('/')
def pull():
    path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(path)
    try:
        output = subprocess.call('git pull', shell=True)
    except Exception as e:
        output = str(dir(e))
        #output += '\n' + str(e.cmd)
        #output += '\n' + str(e.args)
        #output += '\n' + str(e.message)
        #output += '\n' + str(e.output)
        #output += '\n' + str(e.returncode)
        output += '\n' + str(e)
    s = 'pulled at {0}'.format(datetime.now())
    s += '<pre>{0}</pre>'.format(output)
    return s

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6560)
