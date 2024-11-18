from flask import Blueprint, render_template, request, redirect, url_for

connection = None
def enroll_connection(conn):
    global connection
    connection = conn

test = Blueprint('test', __name__)
# 여기는 test code 이므로 db 변경 연산시 rollback 처리


@test.route('/test/department') # , methods=['POST']
def department():
    departments = []
    cursor = connection.cursor()
    cursor.execute("SELECT department_id, department_name FROM department")
    departments = cursor.fetchall()
    return render_template('test/department.html', departments=departments)


#추가 검색기능
@test.route('/test/employee', methods=['GET', 'POST'])
def employee(): 
    cursor = connection.cursor()
    employees = []
    if request.method == 'POST': # 사용자 요청 처리
        if 'add_employee' in request.form:  # 직원 추가 요청
            employee_id = request.form['employee_id']
            department_id = request.form['department_id']
            employee_name = request.form['employee_name']
            registration_number = request.form['registration_number']
            education_level = request.form['education_level']
            skill_set = request.form.get('skill_set', None) # 선택사항
            employee_email = request.form.get('employee_email', None) # 선택사항
            employee_phone_number = request.form.get('employee_phone_number', None) # 선택사항
            employee_address = request.form.get('employee_address', None)
            
            # 튜플 형태로 데이터 생성
            employee_data = (
                employee_id,
                department_id,
                employee_name,
                registration_number,
                education_level,
                skill_set,  # null 가능
                employee_email, # null 가능
                employee_phone_number, # null 가능
                employee_address # null 가능
            )
            
            cursor.execute("""
                INSERT INTO employee (employee_id, department_id, employee_name, registration_number, education_level, skill_set, employee_email)
                VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
            """, employee_data)  # 튜플을 직접 전달
            connection.commit()
            print(f"Added employee: {employee_data}")  # 추가된 직원 확인을 위한 출력
        
        elif 'search_employee' in request.form:  # 직원 검색 요청
            search_name = request.form['search_name'].strip()
            cursor.execute("""
                SELECT employee_id, employee_name, department_name, employee_address, employee_phone_number, employee_email
                FROM employee JOIN department
                ON employee.department_id = department.department_id
                WHERE employee_name LIKE :search_name
            """, {'search_name': '%' + search_name + '%'})
            employees = cursor.fetchall()
            print(f"Searching for: '{search_name}'")  # 결과 확인을 위한 출력
            print(f"Found employees: {employees}")  # 결과 확인을 위한 출력
            
        elif 'delete_employee' in request.form:  # 직원 삭제 요청
            employee_id = request.form['employee_id']
            cursor.execute("""
                DELETE FROM employee
                WHERE employee_id = :employee_id
            """, {'employee_id': employee_id})
            print(f"Deleted employee: {employee_id}") # 삭제된 직원 확인을 위한 출력
            connection.commit()
        else:
            # 다른 POST 요청 처리
            pass
    
    if not employees:  # 직원 목록이 비어있으면 모든 직원 조회
        cursor.execute("""
            SELECT employee_id, employee_name, department_name, employee_address, employee_phone_number, employee_email
            FROM employee JOIN department
            ON employee.department_id = department.department_id
        """)
        employees = cursor.fetchall()
    return render_template('test/employee.html', employees=employees)