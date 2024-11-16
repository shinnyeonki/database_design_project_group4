import os
from flask import Flask
import cx_Oracle
from flask import Blueprint, render_template


ORACLE_INITIALIZED = False

def init_window_oracle_client_driver_config():
    global ORACLE_INITIALIZED
    if not ORACLE_INITIALIZED:
        client_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_6')
        print("Oracle Client Directory:", client_dir)
        try:
            cx_Oracle.init_oracle_client(lib_dir=client_dir)
            print("Oracle Client initialized successfully.")
            ORACLE_INITIALIZED = True
        except cx_Oracle.ProgrammingError:
            ORACLE_INITIALIZED = True
            pass  # 이미 초기화되어 있으면 메시지 출력하지 않고 넘어감

# Oracle Client 초기화
if os.name == 'nt':
    init_window_oracle_client_driver_config()


# 데이터베이스 연결 설정
dsn = cx_Oracle.makedsn("shinnk.iptime.org", 11522, sid="XE")
connection = cx_Oracle.connect(user="db_project_group4", password="1111", dsn=dsn)


app = Flask(__name__)

if __name__ == '__main__':
    # init_oracle_client()
    from views import main
    app.register_blueprint(main) #  main 블루프린트를 애플리케이션에 등록
    app.run(debug=False)