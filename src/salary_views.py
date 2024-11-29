from flask import Blueprint, render_template, request, flash, g
import cx_Oracle

salary = Blueprint('salary', __name__)

# @salary.route('/test/employee', methods=['GET', 'POST'])
# def employee():
#     employees = []
#     employee_to_edit = None
#     try:
#         if request.method == 'POST':
#             if 'add_employee' in request.form:
#                 add_employee()
#             elif 'search_employee' in request.form:
#                 employees = search_employee()
#             elif 'edit_employee' in request.form:
#                 employee_to_edit = edit_employee()
#             elif 'update_employee' in request.form:
#                 update_employee()
#             elif 'delete_employee' in request.form:
#                 delete_employee()
#             else:
#                 flash("Unknown action", 'error')
#         else:
#             employees = get_all_employees()
#     except cx_Oracle.DatabaseError as e:
#         flash(f"Database error: {e}", 'error')
#     return render_template('test/employee.html', employees=employees, employee_to_edit=employee_to_edit)


@salary.route('/test/salary', methods=['GET', 'POST'])
def employee():
    employees = []
    employee_to_edit = None
    try:
        if request.method == 'POST':
            if 'search_employee' in request.form:
                employees = search_employee()
            else:
                flash("Unknown action", 'error')
        else:
            employees = join_employee_salary()
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    return render_template('test/salary.html', employees=employees, employee_to_edit=employee_to_edit)

def search_employee():
    cursor = g.db.cursor()
    search_id = request.form['search_id'].strip()
    cursor.execute("""
        SELECT employee_id, employee_name, salary_id, contract_id, monthly_salary
        FROM employee JOIN salary
        ON employee.employee_id = salary.employee_id
        WHERE employee_id LIKE :search_id
        ORDER BY employee_id
    """, {'search_name': f'%{search_id}%'})
    employees = cursor.fetchall()
    flash(f"Found employees matching '{search_id}'", 'success')
    return employees

def join_employee_salary():
    cursor = g.db.cursor()
    cursor.execute("""
        SELECT employee_id, employee_name, salary_id, contract_id, monthly_salary
        FROM employee JOIN salary
        ON employee.employee_id = salary.employee_id
        ORDER BY employee_id
    """)
    employees = cursor.fetchall()
    return employees