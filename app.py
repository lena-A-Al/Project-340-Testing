
from flask import Flask,render_template, json, redirect,request
from flask_mysqldb import MySQL
# from database import db_connector
import database.db_connector as db
import os


# database connection info
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_aljehanl'
app.config['MYSQL_PASSWORD'] = '8321' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_aljehanl'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)
db_connection = db.connect_to_database()

###----------------------------------Routes---------------------------------------#

#---------------------------------Homepage Request--------------------------------#

@app.route('/')
def index():
    return render_template('/index.html')













#---------------------------------Employee Get Request----------------------------#
@app.route('/employees')
def employees():
    print("Fetching and rending employees web page")
    # db_connection = db_connector.connect_to_database()
    query = "SELECT * from employees;"
    result = db.execute_query(db_connection, query).fetchall()
    print('results employees')    
    return render_template('employees.html', employees=result) 
#---------------------------------------------------------------------------------#

#---------------------------------Employee Add request----------------------------#
@app.route('/add_employee', methods =['POST','GET'])
def add_employee():
    # db_connection = db_connector.connect_to_database()

    if request.method == 'POST':
        print('adding employee')
        manager_id = request.form['manager_id']
        employee_name = request.form['employee_name']
        organization = request.form['organization']
        query = "INSERT INTO employees(manager_id, employee_name, organization) VALUES (%s,%s,%s);"
        data=(manager_id, employee_name, organization)
        db.execute_query(db_connection, query, data).fetchall()
        return redirect("/employees")
    else:
        return render_template('add_employee.html')
#---------------------------------------------------------------------------------#

#---------------------------------Employee Delete request-------------------------#
@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    # db_connection = db_connector.connect_to_database()


    query="DELETE FROM employees WHERE employee_id = %s;"
    data = (id,)
    db.execute_query(db_connection, query, data)
    return redirect("/employees")
#--------------------------------------------------------------------------------#

#---------------------------------Employee Update request------------------------#

@app.route('/employees/edit_employee/<int:id>', methods = ["GET","POST"])
def update_employee(id):
    # db_connection = db_connector.connect_to_database()

    if request.method == "POST":

        manager_id = request.form.get('manager_id')
        employee_name = request.form.get('employee_name')
        organization = request.form.get('organization')
        query2 = "UPDATE employees SET manager_id = %s, employee_name = %s, organization = %s WHERE employee_id= %s;"
        data2= (manager_id, employee_name, organization, id)
        db.execute_query(db_connection, query2, data2)
        return redirect("/employees")

    # Get request 
    else:
        data = (id)
        # Select all managers
        query = "SELECT * FROM managers;"
        managers = db.execute_query(db_connection, query)

        #Get employee data
        query2 = "SELECT * FROM employees WHERE employee_id = %s"
        employee = db.execute_query(db_connection, query).fetchall()
        return render_template("edit_employee.html", employee = employee[0], managers = managers)


#--------------------------------------------------------------------------------#














#---------------------------------Projects Get request---------------------------#
@app.route('/projects')
def projects():
    #Fetching and rendering list of projects
    # db_connection = db_connector.connect_to_database()
    query = "SELECT * from projects;"
    result = db.execute_query(db_connection, query).fetchall()
    print('results projects')    
    return render_template('projects.html', projects=result)
#--------------------------------------------------------------------------------#

#---------------------------------Project Add request----------------------------#
@app.route('/add_project', methods =['POST','GET'])
def add_project():
    # db_connection = db_connector.connect_to_database()

    if request.method == 'POST':
        print('adding project')
        task = request.form['task']
        query = "INSERT INTO projects(task) VALUES (%s);"
        db.execute_query(db_connection, query, task).fetchall()
        return redirect("/projects")
    else:
        return render_template('add_project.html')
#---------------------------------Project Delete request-------------------------#
@app.route('/delete_project/<int:id>')
def delete_project(id):
    # db_connection = db_connector.connect_to_database()

    query="DELETE FROM projects WHERE project_id = %s;"
    db.execute_query(db_connection, query, id)
    return redirect("/projects")
#---------------------------------Project Update request-------------------------#
@app.route('/projects/edit_project/<int:id>', methods = ["GET","POST"])
def update_project(id):
    # db_connection = db_connector.connect_to_database()

    if request.method == "POST":

        task = request.form.get('manager_id')
        query = "UPDATE projects SET task = %s WHERE project_id= %s;"
        data =(task, id)
        db.execute_query(db_connection, query, data)
        return redirect("/projects")

    # Get request 
    else:
        
        #Get employee data
        query2 = "SELECT * FROM projects WHERE project_id = %s"
        project = db.execute_query(db_connection, query2, id).fetchall()
        return render_template("edit_project.html", project = project[0])




#---------------------------------Clients Get request----------------------------#
@app.route('/clients')
def clients():
    # db_connection = db_connector.connect_to_database()
    query = "SELECT * from clients;"
    result = db.execute_query(db_connection, query).fetchall()

    return render_template('clients.html', clients=result)
#--------------------------------------------------------------------------------#

#---------------------------------Client Add request-----------------------------#
@app.route('/add_client', methods =['POST','GET'])
def add_client():
    # db_connection = db_connector.connect_to_database()

    if request.method == 'POST':
        print('adding client')
        project_id = request.form['project_id']
        manager_id = request.form['manager_id']
        client_organization = request.form['client_organization']
        data = (project_id, manager_id, client_organization)
        query = "INSERT INTO clients(project_id, manager_id, client_organization) VALUES (%s,%s,%s);"
        db.execute_query(db_connection, query, data).fetchall()
        return redirect("/clients")
    else:
        return render_template('add_client.html')
#--------------------------------------------------------------------------------#

#---------------------------------Client Delete request--------------------------#
@app.route('/delete_client/<int:id>')
def delete_client(id):
    # db_connection = db_connector.connect_to_database()
    
    query="DELETE FROM clients WHERE client_id = %s;"
    data = (id,)
    db.execute_query(db_connection, query, data)
    return redirect("/clients")

#---------------------------------Client Update request--------------------------#












#---------------------------------Manager Get request----------------------------#
@app.route('/managers')
def managers():
    # db_connection = db_connector.connect_to_database()
    query = "SELECT * from managers;"
    result = db.execute_query(db_connection, query).fetchall()
     
    return render_template('managers.html', managers= result) 
#---------------------------------Manager Add request----------------------------#


#--------------------------------------------------------------------------------#

#---------------------------------Manager Delete request-------------------------#
@app.route('/delete_manager/<int:id>')
def delete_manager(id):
    # db_connection = db_connector.connect_to_database()

    query="DELETE FROM managers WHERE manager_id = %s;"
    db.execute_query(db_connection, query, id)
    return redirect("/managers")
#--------------------------------------------------------------------------------#

#---------------------------------Manager Update request-------------------------#

#--------------------------------------------------------------------------------#







#-------------------------------Projects_mapping Get request---------------------#
@app.route('/projects_mapping')
def projects_mapping():
    db_connection = db.connect_to_database()
    query = "SELECT * from projects_mapping;"
    result = db.execute_query(db_connection, query).fetchall()

    return render_template('projects_mapping.html', projects_mapping = result)
#--------------------------------------------------------------------------------#

#---------------------------------Project_mapping Add request--------------------#
"""Once you fix your table attributes you can tackle this without issues"""
@app.route('/add_project_mapping', methods =['POST','GET'])
def add_project_mapping():
    # db_connection = db_connector.connect_to_database()

    if request.method == 'POST':
        print('adding employee')
        task = request.form['task']
        query = "INSERT INTO projects(task) VALUES (%s);"
        data=(task)
        db.execute_query(db_connection, query, data).fetchall()
        return redirect("/projects")
    else:
        return render_template('add_employee.html')
#---------------------------------Project_mapping Delete request-----------------#
@app.route('/delete_project/<int:id>')
def delete_project_mapping(id):
    # db_connection = db_connector.connect_to_database()
    """You need to review your project mapping table because you cannot delete based on
    employee id or project id. You need to have a primary key on this table to delete items
    properly
    """
    query="DELETE FROM projects_mapping WHERE {{need a better attrbute here}} = %s;"
    db.execute_query(db_connection, query, id)
    return redirect("/projects_mapping")
#---------------------------------Project_mapping Update request-----------------#
#--------------------------------------------------------------------------------#

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 42543))
    app.run(port=port, debug=False)