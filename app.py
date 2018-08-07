# from flask import Flask

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World Vital xxx!'

print(">>>> route foo")
@app.route('/foo')
def hello_foo():
    return 'Hello World FOO!'

print(">>>> route bar")
@app.route('/bar')
def hello_bar():
    return 'Hello World BAR2!'

if __name__ == '__main__':
    app.run(debug=True)

