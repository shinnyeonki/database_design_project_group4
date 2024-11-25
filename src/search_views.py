from flask import Blueprint, render_template, request, flash, g, session
import cx_Oracle

search_em = Blueprint('search_em', __name__)

@search_em.route('/search', methods=['GET', 'POST'])
def search():
    employees = []
    employee_detail = None
    # 이전 flash 메시지 초기화
    session.pop('_flashes', None)  # flash 메시지 초기화
    try:
        if request.method == 'POST':
            if 'search_employee' in request.form:
                # 검색 파라미터 가져오기
                search_name = request.form.get('search_name')
                search_department = request.form.get('search_department')
                search_position = request.form.get('search_position')
                search_login_id = request.form.get('search_login_id')

                # 모든 검색 파라미터가 None인지 확인
                if not search_name and not search_department and not search_position and not search_login_id:
                    flash("적어도 하나의 검색 조건을 입력해야 합니다.", 'error')
                else:
                    # 쿼리 빌드
                    query = """
                        SELECT e.username, e.employee_name, d.department_name,
                               COUNT(pp.project_id) AS current_projects
                        FROM employee e
                        JOIN department d ON e.department_id = d.department_id
                        LEFT JOIN participation_project pp ON e.employee_id = pp.employee_id AND pp.end_date IS NULL
                        WHERE 1=1
                    """
                    params = {}
                    if search_name:
                        query += " AND e.employee_name LIKE :employee_name"
                        params['employee_name'] = f"%{search_name}%"
                    if search_department:
                        query += " AND d.department_name LIKE :department_name"
                        params['department_name'] = f"%{search_department}%"
                    if search_position:
                        query += " AND pp.role LIKE :role"
                        params['role'] = f"%{search_position}%"
                    if search_login_id:
                        query += " AND e.username LIKE :username"
                        params['username'] = f"%{search_login_id}%"

                    query += " GROUP BY e.username, e.employee_name, d.department_name"
                    # 쿼리 실행
                    cursor = g.db.cursor()
                    cursor.execute(query, params)
                    employees = cursor.fetchall()
                    cursor.close()
            elif 'fetch_employee' in request.form:
                employee_id = request.form.get('employee_id')
                # 직원 세부정보 가져오기
                cursor = g.db.cursor()
                cursor.execute("""
                    SELECT e.username, e.employee_name, d.department_name,
                           (SELECT COUNT(*) FROM participation_project pp WHERE pp.employee_id = e.employee_id) AS project_count,
                           e.education_level, e.skill_set, e.employee_email, e.employee_phone_number, e.employee_address,
                           (SELECT c.annual_salary FROM contract c WHERE c.employee_id = e.employee_id ORDER BY c.contract_date DESC FETCH FIRST 1 ROWS ONLY) AS current_salary
                    FROM employee e
                    JOIN department d ON e.department_id = d.department_id
                    WHERE e.username = :username
                """, {'username': employee_id})
                employee_detail = cursor.fetchone()
                cursor.close()
            else:
                flash("알 수 없는 작업입니다.", 'error')
        else:
            # GET 요청일 때 모든 직원 정보 가져오기
            cursor = g.db.cursor()
            cursor.execute("""
                SELECT e.username, e.employee_name, d.department_name,
                       COUNT(pp.project_id) AS current_projects
                FROM employee e
                JOIN department d ON e.department_id = d.department_id
                LEFT JOIN participation_project pp ON e.employee_id = pp.employee_id AND pp.end_date IS NULL
                GROUP BY e.username, e.employee_name, d.department_name
            """)
            employees = cursor.fetchall()
            cursor.close()
        
    except cx_Oracle.DatabaseError as e:
        flash(f"데이터베이스 오류: {e}", 'error')
        
    return render_template('search.html', employees=employees, employee_detail=employee_detail)
