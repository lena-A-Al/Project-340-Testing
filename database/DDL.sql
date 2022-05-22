SET FOREIGN_KEY_CHECKS=0;
SET AUTOCOMMIT = 0;


DROP TABLES IF EXISTS clients, employees, projects, projects_mapping, managers;

--Table structure for table managers
CREATE TABLE managers (
  manager_id int(11) NOT NULL AUTO_INCREMENT,
  manager_name varchar(30) NOT NULL UNIQUE,
  organization varchar(30) NOT NULL,
  PRIMARY KEY (manager_id)
);

-- -- Table structure for table projects
CREATE TABLE projects (
  project_id int(11) NOT NULL AUTO_INCREMENT,
  task varchar(50) NOT NULL,
  PRIMARY KEY(project_id)
);

-- Table structure for table clients
CREATE TABLE clients (
  client_id int(11) NOT NULL AUTO_INCREMENT,
  project_id int(11) NOT NULL,
  manager_id int(11) NOT NULL,
  client_organization varchar(30) NOT NULL,
  PRIMARY KEY (client_id),
  FOREIGN KEY (manager_id) REFERENCES managers (manager_id) ON UPDATE CASCADE,
  FOREIGN KEY (project_id) REFERENCES projects (project_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- -- Table structure for table employees
CREATE TABLE employees (
  employee_id int(11) NOT NULL AUTO_INCREMENT,
  manager_id int(11) NOT NULL,
  employee_name varchar(30) NOT NULL,
  organization varchar(30) NOT NULL,
  PRIMARY KEY (employee_id),
  FOREIGN KEY (manager_id) REFERENCES managers (manager_id) ON DELETE CASCADE ON UPDATE CASCADE
);


-- Table structure for table projects_mapping
CREATE TABLE projects_mapping (
  employee_id int(11) DEFAULT NULL,
  project_id int(11) NOT NULL,
  PRIMARY KEY (project_id, employee_id),
  FOREIGN KEY(employee_id) REFERENCES employees (employee_id),
  FOREIGN KEY(project_id) REFERENCES projects (project_id)
);

-- Insert values into managers tables

INSERT INTO managers
(
manager_name, organization
)
VALUES ('Josh Porter','marketing'),('Jan Levinson','legal'),('Toby Flenderson','HR');

--Insert values into employees table

INSERT INTO employees (manager_id,employee_name,organization)
VALUES (
(SELECT manager_id FROM managers WHERE manager_id=1), 
'Dwight Shrute',
(SELECT organization FROM managers WHERE manager_id=1)),

(
(SELECT manager_id FROM managers WHERE manager_id=1), 
'Karen Filapeli',
(SELECT organization FROM managers WHERE manager_id=1)),

(
(SELECT manager_id FROM managers WHERE manager_id=3), 
'Creed Bratton',
(SELECT organization FROM managers WHERE manager_id=3)),

(
(SELECT manager_id FROM managers WHERE manager_id=2), 
'Michael Scott',
(SELECT organization FROM managers WHERE manager_id=2)),

(
(SELECT manager_id FROM managers WHERE manager_id=3),
'Andy Bernard',
(SELECT organization FROM managers WHERE manager_id=3));

INSERT INTO projects (task)
VALUES ('Fix brochure design'),('Update HR policy on gun violence'),('fix our liability policies'),
('design new commercial for new product');


INSERT INTO clients (project_id, manager_id, client_organization)
VALUES
(
(SELECT project_id FROM projects WHERE project_id=2), 
(SELECT manager_id FROM managers WHERE manager_id=3),  
(SELECT organization FROM managers WHERE manager_id=3)
),
(
(SELECT project_id FROM projects WHERE project_id=1),  
(SELECT manager_id FROM managers WHERE manager_id=2), 
(SELECT organization FROM managers WHERE manager_id=1)
),
(
(SELECT project_id FROM projects WHERE project_id=4),  
(SELECT manager_id FROM managers WHERE manager_id=1), 
(SELECT organization FROM managers WHERE manager_id=1)
),
(
(SELECT project_id FROM projects WHERE project_id=3), 
(SELECT manager_id FROM managers WHERE manager_id=2), 
(SELECT organization FROM managers WHERE manager_id=2)
);

INSERT INTO projects_mapping (employee_id,project_id)
VALUES
(
  (SELECT employee_id FROM employees WHERE employee_id=1),
  (SELECT project_id FROM projects WHERE project_id=1)
),
(
  (SELECT employee_id FROM employees WHERE employee_id=1),
  (SELECT project_id FROM projects WHERE project_id=4)
),
(
  (SELECT employee_id FROM employees WHERE employee_id=2),
  (SELECT project_id FROM projects WHERE project_id=4)
),
(
  (SELECT employee_id FROM employees WHERE employee_id=3),
  (SELECT project_id FROM projects WHERE project_id=2)
),
(
  (SELECT employee_id FROM employees WHERE employee_id=5),
  (SELECT project_id FROM projects WHERE project_id=2)
),
(
  (SELECT employee_id FROM employees WHERE employee_id=4),
  (SELECT project_id FROM projects WHERE project_id=3)
),
(
  NULL,
  (SELECT project_id FROM projects WHERE project_id=3)
);

SET FOREIGN_KEY_CHECKS=1;
COMMIT;