import boto3
from boto3 import resource
import config


AWS_ACCESS_KEY_ID = config.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = config.AWS_SECRET_ACCESS_KEY
REGION_NAME = config.REGION_NAME

resource = resource(
   'dynamodb',
   aws_access_key_id     = AWS_ACCESS_KEY_ID,
   aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
   region_name           = REGION_NAME
)

dynamo_client = boto3.client('dynamodb')

def get_departments():
    return dynamo_client.scan(
        TableName='Department'
    )
    
EmployeesTable = resource.Table('Employees')
DepartmentTable = resource.Table('Department')

def get_employee():
    return dynamo_client.scan(
        TableName='Employees'
    )
    
def get_department(department_id):
    response = DepartmentTable.get_item(
    Key={
        'DepartmentID': department_id
        }
    )
    print(response['Item'])
    return response['Item']
    
def get_employee_from_department(department_id):
    response = get_employee()
    base_profile_url = 'peoplesuite/apis/employees/'
    employee_data = [
    {
        'employee_id': item['EmployeeID']['S'],
        'employee_name': item['FirstName']['S'] + " " + item['LastName']['S'],
        'employee_profile_url': base_profile_url + item['EmployeeID']['S']
    }
    for item in response['Items']
    if item['DepartmentID']['S'] == department_id
]
    return employee_data
    


    
    

    
    


