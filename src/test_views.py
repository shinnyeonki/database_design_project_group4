from flask import Blueprint, render_template, request, redirect, url_for, flash
import cx_Oracle

connection = None
def enroll_connection(conn):
    global connection
    connection = conn

test = Blueprint('test', __name__)

@test.route('/test/department') # , methods=['POST']
def department():
    departments = []
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT department_id, department_name FROM department")
        departments = cursor.fetchall()
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')
    return render_template('test/department.html', departments=departments)

@test.route('/test/employee', methods=['GET', 'POST'])
def employee(): 
    cursor = connection.cursor()
    employees = []
    employee_to_edit = None
    if request.method == 'POST':
        try:
            if 'add_employee' in request.form:
                add_employee(request, cursor)
            elif 'search_employee' in request.form:
                employees = search_employee(request, cursor)
            elif 'edit_employee' in request.form:
                employee_to_edit = edit_employee(request, cursor)
            elif 'update_employee' in request.form:
                update_employee(request, cursor)
            elif 'delete_employee' in request.form:
                delete_employee(request, cursor)
            else:
                flash("Unknown action", 'error')
        except cx_Oracle.DatabaseError as e:
            flash(f"Database error: {e}", 'error')
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')
    else:
        try:
            cursor.execute("""
                SELECT employee_id, employee_name, department_name, employee_address, employee_phone_number, employee_email
                FROM employee JOIN department
                ON employee.department_id = department.department_id
                ORDER BY employee_id
            """)
            employees = cursor.fetchall()
        except cx_Oracle.DatabaseError as e:
            flash(f"Database error: {e}", 'error')
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')
    return render_template('test/employee.html', employees=employees, employee_to_edit=employee_to_edit)

def add_employee(request, cursor):
    try:
        employee_id = request.form['employee_id']
        department_id = request.form['department_id']
        employee_name = request.form['employee_name']
        registration_number = request.form['registration_number']
        education_level = request.form['education_level']
        skill_set = request.form.get('skill_set', None)
        employee_email = request.form.get('employee_email', None)
        employee_phone_number = request.form.get('employee_phone_number', None)
        employee_address = request.form.get('employee_address', None)
        
        employee_data = (
            employee_id,
            department_id,
            employee_name,
            registration_number,
            education_level,
            skill_set,
            employee_email,
            employee_phone_number,
            employee_address
        )
        
        cursor.execute("""
            INSERT INTO employee (employee_id, department_id, employee_name, registration_number, education_level, skill_set, employee_email, employee_phone_number, employee_address)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
        """, employee_data)
        connection.commit()
        flash(f"Added employee: {employee_data}", 'success')
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')

def search_employee(request, cursor):
    try:
        search_name = request.form['search_name'].strip()
        cursor.execute("""
            SELECT employee_id, employee_name, department_name, employee_address, employee_phone_number, employee_email
            FROM employee JOIN department
            ON employee.department_id = department.department_id
            WHERE employee_name LIKE :search_name
            ORDER BY employee_id
        """, {'search_name': '%' + search_name + '%'})
        employees = cursor.fetchall()
        flash(f"Searching for: '{search_name}'", 'success')
        flash(f"Found employees: {employees}", 'success')
        return employees
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')

def edit_employee(request, cursor):
    try:
        employee_id = request.form['edit_employee_id']
        cursor.execute("""
            SELECT employee_id, employee_name, department_id, registration_number, education_level, skill_set, employee_email, employee_phone_number, employee_address
            FROM employee
            WHERE employee_id = :employee_id
        """, {'employee_id': employee_id})
        employee_to_edit = cursor.fetchone()
        flash(f"Fetching employee: {employee_id}", 'success')
        return employee_to_edit
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')

def update_employee(request, cursor):
    try:
        employee_id = request.form['employee_id']
        employee_name = request.form['employee_name']
        department_id = request.form['department_id']
        registration_number = request.form['registration_number']
        education_level = request.form['education_level']
        skill_set = request.form.get('skill_set', None)
        employee_email = request.form.get('employee_email', None)
        employee_phone_number = request.form.get('employee_phone_number', None)
        employee_address = request.form.get('employee_address', None)

        cursor.execute("""
            UPDATE employee
            SET employee_name = :employee_name,
                department_id = :department_id,
                registration_number = :registration_number,
                education_level = :education_level,
                skill_set = :skill_set,
                employee_email = :employee_email,
                employee_phone_number = :employee_phone_number,
                employee_address = :employee_address
            WHERE employee_id = :employee_id
        """, {
            'employee_name': employee_name,
            'department_id': department_id,
            'registration_number': registration_number,
            'education_level': education_level,
            'skill_set': skill_set,
            'employee_email': employee_email,
            'employee_phone_number': employee_phone_number,
            'employee_address': employee_address,
            'employee_id': employee_id
        })
        connection.commit()
        flash(f"Updated employee: {employee_id}", 'success')
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')

def delete_employee(request, cursor):
    try:
        employee_id = request.form['employee_id']
        cursor.execute("""
            DELETE FROM employee
            WHERE employee_id = :employee_id
        """, {'employee_id': employee_id})
        connection.commit()
        flash(f"Deleted employee: {employee_id}", 'success')
    except cx_Oracle.DatabaseError as e:
        flash(f"Database error: {e}", 'error')
    except Exception as e:
        flash(f"An error occurred: {e}", 'error')