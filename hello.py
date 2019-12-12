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

# html 태그를 리턴
@app.route('/html_tag')
def html_tag():
    return '<h1>안녕하세요</h1>'

# html 문서를 리턴
@app.route('/html_file')
def html_file():
    return render_template('index.html')

# 변수를 만들고 전달한 뒤 html 문서 리턴
@app.route('/variable')
def variable():
    name = "권윤옥"
    return render_template('variable.html', html_name=name )

# 동적 라우팅
@app.route('/greeting/<string:name>/')
def greeting(name):
    def_name = name
    return render_template('greeting.html', html_name=def_name)

# '/cube/3' > 결과: 3의 세제곱은 27입니다.
@app.route('/cube/<int:number>/')
def cube(number):
    # cube_num = number ** 3
    def_number = number
    ## 연산은 백엔드에서 완료한 후에 변수만 전달하는 것이 좋음
    # return render_template('cube.html', html_number=def_number, cube_num=cube_num)
    return render_template('cube.html', html_number=def_number)

if __name__ == '__main__':
    # debug=True: 개발자 모드를 켜놔서 저장할때마다 서버에 반영이 됨
    app.run(debug=True)
