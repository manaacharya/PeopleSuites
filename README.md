# PeopleSuites

## An end-to-end cloud native SAAS application connected to AWS S3 and AWS dynamoDB

### To run Employee Microservice 
```flask run``` employees folder app.py

/peoplesuite/apis/employees/{EmployeeID}/profile GET returns Employee Profile stored in DynamoDB table 
EmployeeID 
First Name
Last Name
Start Date 
Country 
DepartmentID 
Title
Manager ID 
Manager Name 

/peoplesuite/apis/employees/{EmployeeID}/photo GET returns Employee profile pictures (stock images) stored in S3 bucket Employees


### To run Departments Microservice 
```flask run``` department folder app.py 
GET /peoplesuite/apis/departments returns Department profile 
DepartmentID 
CostCenter 
Parent DepartmentID 

GET /peoplesuite/apis/departments/{departmentId}/employees returns the following details of each employee in the department
Employee ID (7 digits))
Employee Name
Employee Profile URL

### batch-write.json, create-table.json, config.py and aws_controller.py are included in each microservies to build dynamoDB tables and access to AWS Cloud services (now inactive) 

Python, Flask, HTML, DynamoDB, S3, DOCKER and Kubernetes used to create this project. 



