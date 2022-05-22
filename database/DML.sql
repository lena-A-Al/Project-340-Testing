
-------------------------------------- All managers queries ------------------------------------------------------------------------------
-- create: managers
INSERT INTO managers (manager_name, organization) VALUES (:manager_name_input, :manager_org_input)

-- read: managers
SELECT * FROM managers

-- read: Single manager for the purpose of updating
SELECT manager_name, organization FROM managers WHERE manager_id = manager_id_selected

-- Update: manager organization
UPDATE managers SET organization= :new_organization WHERE manager_id = manager_id_selected


-------------------------------------- All clients queries --------------------------------------------------------------------------
-- create: clients
INSERT INTO clients (project_id, manager_id, client_organization) VALUES 
(:project_id_selected, :manager_id_selected, :client_org)

-- read: clients
SELECT * FROM clients

-- read: single client
SELECT project_id, manager_id, client_organization FROM clients WHERE project_id = :project_id_selected

-- update: clients
UPDATE clients SET manager_id = :manager_id_selected

-- delete: clients
DELETE FROM clients WHERE client_id = :client_id_selected


-------------------------------------- All projects queries -----------------------------------------------------------------------
-- create: project
INSERT INTO projects(task) VALUES (:task_description_selected)

-- read: project
SELECT * FROM projects

-- select: single project
SELECT project_id from projects WHERE project_id= :project_id_selected

-- update: projects
UPDATE projects SET task = :task_description_selected WHERE project_id=:project_id_selected

-- delete: projects
DELETE FROM projects WHERE project_id = :project_id_selected


-------------------------------------- All employees queries -------------------------------------------------------------------------------
-- create: employees
INSERT INTO employees (manager_id, employee_name, organization) VALUES (:manager_id_selected, :employee_name_selected, :organization_selected)

-- read: employees
SELECT * FROM employees

-- select a single employee for updating and deleting
SELECT manager_id, employee_name, organization FROM employees WHERE employee_id = :employee_id_selected

-- update: employee
UPDATE employees SET manager_id = :manager_id_selected

-- delete: employee
DELETE FROM employees WHERE employee_id = :employee_id_selected


-------------------------------------- All projects_mapping queries --------------------------------------------------------------------------
INSERT INTO projects_mapping (employee_id,project_id) VALUES (:employee_id_selected,:project_id_selected)

--read: projects_mapping
SELECT * FROM projects_mapping

--select a single project for updating and deleting
SELECT employee_id, project_id FROM projects_mapping WHERE project_id = :project_id_selected

--update: employee assigned to project
UPDATE projects_mapping SET employee_id = :employee_id_selected WHERE project_id = :project_id_selected
