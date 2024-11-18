import os
from flask import Flask
import platform
import cx_Oracle

app = Flask(__name__)

if __name__ == '__main__':
    if os.name == "nt":
        cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_6'))
    elif os.name == "posix":
        if platform.system() == "Linux":
            cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_6'))
        elif platform.system() == "Darwin":  # macOS는 Darwin으로 식별됩니다.
            cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_3'))
    dsn = cx_Oracle.makedsn("shinnk.iptime.org", 11522, sid="XE")
    connection = cx_Oracle.connect(user="db_project_group4", password="1111", dsn=dsn)
    from views import main, enroll_connection
    enroll_connection(connection) # 연결 설정
    app.register_blueprint(main) #  main 블루프린트를 애플리케이션에 등록
    app.run(debug=True)