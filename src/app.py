import os
from flask import Flask
import platform
import cx_Oracle

app = Flask(__name__)

if __name__ == '__main__':
    # 드라이버 로드
    if os.name == "nt":
        cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_6'))
    elif os.name == "posix":
        if platform.system() == "Linux":
            cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_6'))
        elif platform.system() == "Darwin":  # macOS는 Darwin으로 식별됩니다.
            cx_Oracle.init_oracle_client(lib_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'instantclient_23_3'))
    
    # 데이터베이스 연결
    # 공용 db 서버
    connection = cx_Oracle.connect(user="db_project_group4", password="1111", dsn="shinnk.iptime.org:11522/XE")
    # 개인 db 사용하고 싶으면 아래 주석 해제
    # connection = cx_Oracle.connect(user="class_c", password="????", dsn="localhost:1521/XE")
    
    
    #블루 프린트 설정
    import views
    import test_views
    views.enroll_connection(connection) # 연결 설정
    app.register_blueprint(views.main) #  main 블루프린트를 애플리케이션에 등록
    test_views.enroll_connection(connection) # 연결 설정
    app.register_blueprint(test_views.test) #  test 블루프린트를 애플리케이션에 등록
    
    
    app.run(debug=True, port=5010)