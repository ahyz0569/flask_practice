from flask import Flask, escape, request, render_template

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

#html 태그를 리턴
@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

#html 문서를 리턴
@app.route('/html_file')
def html_file():
    return render_template('index.html')

#변수를 만들고 전달한 뒤 html 문서 리턴
@app.route('/variable')
def variable():
    name = "권윤옥"
    return render_template('variable.html', html_name=name )

if __name__ == '__main__':
    # debug=True: 개발자 모드를 켜놔서 저장할때마다 서버에 반영이 됨
    app.run(debug=True)
