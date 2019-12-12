from flask import Flask, escape, request, render_template
import random

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

# 점심메뉴 추천
@app.route('/lunch')
def lunch():
    lunch_menu= ['20층A 부대찌개','20층B','양자강','소풍라면','솥뚜껑볶음밥']
    lunch_menu_link=[
        'http://recipe1.ezmember.co.kr/cache/recipe/2018/02/27/b5806f01ccb6f6d5d9aa94bdd6f4287e1.jpg',
        'http://recipe1.ezmember.co.kr/cache/recipe/2016/10/27/b58a96509ce8f9dfad2026e8ed94da501.jpg',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/480px-Jajangmyeon_by_stu_spivack.jpg',
        'https://w.namu.la/s/9f15f198aab1b14c8aa47e96a91a9d03331ecb7b5b892c803159d39b0d77ab4be30e2f15f66191284d7dad8371989329cc1c80810745e980a6949ae5e3589df6c8ec8d9c1600747b4316c05ef597395eaf0d4bf5a1613c576641c18c9be5bb67',
        'https://t1.daumcdn.net/cfile/tistory/991CD24B5C9791BD2D'
    ]

    lunch = random.choice(lunch_menu)
    for i in range(0, 5):
        if lunch == lunch_menu[i]:
            lunch_img = lunch_menu_link[i]
    # return render_template('lunch.html', lunch=lunch, lunch_img=lunch_img )


    #dictionary를 사용해서 실행해보자
    menus = { 
        "짜장면" : 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Jajangmyeon_by_stu_spivack.jpg/480px-Jajangmyeon_by_stu_spivack.jpg',
        "부대찌개" : 'http://recipe1.ezmember.co.kr/cache/recipe/2018/02/27/b5806f01ccb6f6d5d9aa94bdd6f4287e1.jpg',
        "소풍라면" : 'https://w.namu.la/s/9f15f198aab1b14c8aa47e96a91a9d03331ecb7b5b892c803159d39b0d77ab4be30e2f15f66191284d7dad8371989329cc1c80810745e980a6949ae5e3589df6c8ec8d9c1600747b4316c05ef597395eaf0d4bf5a1613c576641c18c9be5bb67'
    }

    menu_list = list(menus.keys())
    pick = random.choice(menu_list)
    img = menus[pick]

    return render_template('lunch.html', lunch=pick, lunch_img=img )

# 
@app.route('/movies')
def movies():
    movies = ['겨울왕국2', '나이브스아웃', '포드v페라리']
    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    # debug=True: 개발자 모드를 켜놔서 저장할때마다 서버에 반영이 됨
    app.run(debug=True)
