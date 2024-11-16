from flask import Flask
import cx_Oracle
from flask import Blueprint, render_template


# 데이터베이스 연결 설정
dsn = cx_Oracle.makedsn("shinnk.iptime.org", 11522, sid="XE")
connection = cx_Oracle.connect(user="db_project_group4", password="1111", dsn=dsn)

app = Flask(__name__)

if __name__ == '__main__':
    from views import main
    app.register_blueprint(main) #  main 블루프린트를 애플리케이션에 등록
    app.run(debug=True)