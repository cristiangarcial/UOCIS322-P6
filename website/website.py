from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    render_template('index.html')

@app.route('/listall')
def listAll():
    r = requests.get('http://restapi:5000/listAll')
    return r.text

@app.route('/listOpenOnly')
def listOpenOnly():
    r = requests.get('http://restapi:5000/listOpenOnly')
    return r.text

@app.route('/listCloseOnly')
def listCloseOnly():
    r = requests.get('http://restapi:5000/listCloseOnly')
    return r.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
