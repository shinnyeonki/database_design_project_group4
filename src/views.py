from flask import Blueprint, render_template

connection = None
def enroll_connection(conn):
    global connection
    connection = conn

main = Blueprint('main', __name__)

@main.route('/')
def index(): #연결 test 및 home.html 렌더링
    return render_template('home.html')

@main.route('/department') # , methods=['POST']
def department():
    departments = []
    cursor = connection.cursor()
    cursor.execute("SELECT department_id, department_name FROM department")
    departments = cursor.fetchall()
    return render_template('department.html', departments=departments)

@main.route('/employee')
def employee(): # 조인 연산 test
    employees = [] # 유저 id, 부서명, 이름
    cursor = connection.cursor()
    cursor.execute("""
        SELECT employee_id, employee_name, department_name, employee_address, employee_phone_number, employee_email
        FROM employee JOIN department
        ON employee.department_id = department.department_id
    """)
    employees = cursor.fetchall()
    return render_template('employee.html', employees=employees)

