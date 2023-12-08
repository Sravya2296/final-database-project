from bottle import route, run, template, request, redirect
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Routes
@route('/')
def index():
    return template('index.tpl')

@route('/employees')
def employees():
    cursor.execute('SELECT * FROM employee')
    result = cursor.fetchall()
    return template('employees.tpl', employees=result)

@route('/add_employee', method='POST')
def add_employee():
    name = request.forms.get('name')
    organization_id = request.forms.get('organization_id')
    cursor.execute('INSERT INTO employee (name, organization_id) VALUES (?, ?)', (name, organization_id))
    conn.commit()
    return redirect('/employees')

@route('/edit_employee/<id>', method='GET')
def edit_employee(id):
    cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))
    result = cursor.fetchone()
    return template('edit_employee.tpl', employee=result)

@route('/update_employee/<id>', method='POST')
def update_employee(id):
    name = request.forms.get('name')
    organization_id = request.forms.get('organization_id')
    cursor.execute('UPDATE employee SET name=?, organization_id=? WHERE id=?', (name, organization_id, id))
    conn.commit()
    return redirect('/employees')

@route('/delete_employee/<id>', method='GET')
def delete_employee(id):
    cursor.execute('DELETE FROM employee WHERE id = ?', (id,))
    conn.commit()
    return redirect('/employees')

@route('/search', method='GET')
def search_employee():
    query = request.query.get('query')
    cursor.execute("SELECT * FROM employee WHERE name LIKE ?", ('%' + query + '%',))
    result = cursor.fetchall()
    return template('employees.tpl', employees=result)

if __name__ == "__main__":
    run(host='localhost', port=8086)
