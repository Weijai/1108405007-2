from flask import Flask

app = Flask(__name__)

@app.route('/<int:userid>')
def hello(userid):
    return 'Hello, World id = {}' .format (userid)

@app.route('/test1')
def test1():
    return 'Hello, World!'


if __name__ == '__main__':
    app.debug =True
app.run(debug=True, host='127.0.0.1', port=5000)