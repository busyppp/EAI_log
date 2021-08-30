from flask import Flask, render_template, request
import psycopg2



#sql_log = "select * from public.eai_trans_log order by proc_time desc"
#cur.execute(sql_log)
#log_data_list = cur.fetchall()

#sql_mon = "select * from public.eai_trans_mon order by proc_time desc"
#cur.execute(sql_mon)
#mon_data_list = cur.fetchall()


app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def eai_log():
    if request.method == 'POST':
        tran_id = request.form['tran_id']
        con = psycopg2.connect(host='localhost', dbname='postgres', user='postgres', password='1111', port='5432')
        cur1 = con.cursor()
        cur1.execute(f"select * from public.eai_trans_log where tran_id like ('%{tran_id}%') order by proc_time desc")
        #cur1.execute(f"select * from public.eai_trans_log order by proc_time desc")
        log_data_list = cur1.fetchall()
        cur2 = con.cursor()
        cur2.execute(f"select * from public.eai_trans_mon where tran_id like ('%{tran_id}%') order by proc_time desc")
        #cur2.execute(f"select * from public.eai_trans_mon order by proc_time desc")
        mon_data_list = cur2.fetchall()
        return render_template("pgsql.html", log_data_list=log_data_list, mon_data_list=mon_data_list)
    else:
        return render_template("pgsql.html")

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

if __name__ == '__main__':
    app.run(debug=True)