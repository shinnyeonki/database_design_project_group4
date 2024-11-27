from flask import Blueprint, render_template, request, flash, g, session
import cx_Oracle

search_em = Blueprint('search_em', __name__)

def get_search_params():
    return {
        'search_name': request.form.get('search_name'),
        'search_department': request.form.get('search_department'),
        'search_position': request.form.get('search_position'),
        'search_login_id': request.form.get('search_login_id')
    }

def build_search_query(params):
    query = """
        SELECT e.username,
            e.employee_name,
            d.department_name,
            COUNT(pp.project_id) AS current_projects
        FROM employee e
        JOIN department d ON e.department_id = d.department_id
        LEFT JOIN participation_project pp ON e.employee_id = pp.employee_id AND pp.end_date IS NULL
        WHERE 1=1
    """
    bind_params = {}
    if params['search_name']:
        query += " AND e.employee_name LIKE :employee_name"
        bind_params['employee_name'] = f"%{params['search_name']}%"
    if params['search_department']:
        query += " AND d.department_name LIKE :department_name"
        bind_params['department_name'] = f"%{params['search_department']}%"
    if params['search_position']:
        query += " AND pp.role LIKE :role"
        bind_params['role'] = f"%{params['search_position']}%"
    if params['search_login_id']:
        query += " AND e.username LIKE :username"
        bind_params['username'] = f"%{params['search_login_id']}%"
    query += " GROUP BY e.username, e.employee_name, d.department_name"
    return query, bind_params

def execute_query(query, params):
    cursor = g.db.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    return results

def fetch_employee_detail(employee_id):
    cursor = g.db.cursor()
    cursor.execute("""
        SELECT e.username,
            e.employee_name,
            d.department_name,
            (SELECT COUNT(*) FROM participation_project pp WHERE pp.employee_id = e.employee_id) AS project_count,
            e.education_level, 
            e.skill_set, 
            e.employee_email, 
            e.employee_phone_number, 
            e.employee_address,
            (SELECT c.annual_salary FROM contract c WHERE c.employee_id = e.employee_id ORDER BY c.contract_date DESC FETCH FIRST 1 ROWS ONLY) AS current_salary
        FROM employee e
        JOIN department d ON e.department_id = d.department_id
        WHERE e.username = :username
    """, {'username': employee_id})
    employee_detail = cursor.fetchone()
    cursor.close()
    return employee_detail

@search_em.route('/search', methods=['GET', 'POST'])
def search():
    employees = []
    employee_detail = None
    session.pop('_flashes', None)  # flash 메시지 초기화
    try:
        if request.method == 'POST':
            if 'search_employee' in request.form:
                search_params = get_search_params()
                if not any(search_params.values()):
                    flash("적어도 하나의 검색 조건을 입력해야 합니다.", 'error')
                else:
                    query, params = build_search_query(search_params)
                    employees = execute_query(query, params)
                    session['search_params'] = search_params
            elif 'fetch_employee' in request.form:
                employee_id = request.form.get('employee_id')
                employee_detail = fetch_employee_detail(employee_id)
                search_params = session.get('search_params', {})
                query, params = build_search_query(search_params)
                employees = execute_query(query, params)
        else:
            query = """
                SELECT e.username,
                    e.employee_name,
                    d.department_name,
                    COUNT(pp.project_id) AS current_projects
                FROM employee e
                JOIN department d ON e.department_id = d.department_id
                LEFT JOIN participation_project pp ON e.employee_id = pp.employee_id AND pp.end_date IS NULL
                GROUP BY e.username, e.employee_name, d.department_name
            """
            employees = execute_query(query, {})
    except cx_Oracle.DatabaseError as e:
        flash(f"데이터베이스 오류: {e}", 'error')
        
    return render_template('search.html', employees=employees, employee_detail=employee_detail)