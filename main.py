from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return '''
    <h1>이건 h1 제목</h1>
    <p>이건 p 본문 </p>
    <a href="https://flask.palletsprojects.com">Flask 홈페이지 바로가기</a><br>
    <a href="/html1"> pgsql 바로가기</a>
    '''
@app.route('/user/<user_name>/<user_id>')
def user(user_name, user_id):
    return f'Hello, {user_name} {user_id}!'

@app.route('/')
def html1():
    return render_template("home.html")



if __name__ == '__main__':
    app.run(debug=True)