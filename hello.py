from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/hi')
def hi():
    return 'hi'

@app.route('/yunok')
def yunok():
    return 'hello yunok'

if __name__ == '__main__':
    app.run(debug=True)
