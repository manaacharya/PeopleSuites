import boto3
from boto3 import resource
import config
import uuid
from flask import Flask, render_template, request, send_file
import base64

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
UPLOAD_FOLDER = "uploads"
BUCKET = "lab7-images-data"
s3 = boto3.client('s3')


def get_employee_picture(employee_id):
    image_name = employee_id + ".jpeg"
    try:
        response = s3.get_object(Bucket=BUCKET, Key=image_name)
        image_data = response['Body'].read()
        image_base64 = base64.b64encode(image_data).decode('utf-8')
        
        return render_template('image.html', image_data=image_base64)
    except Exception as e:
        return str(e), 404

def upload_file(file_name, bucket):
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def get_employees():
    return dynamo_client.scan(
        TableName='Employees'
    )
    
EmployeesTable = resource.Table('Employees')

def write_to_employees(id, first_name, last_name, start_date, country, department_ID, title, manager_ID, manager_name):
    response = EmployeesTable.put_item(
        Item = {
            'EmployeeID' : id,
            'FirstName' : first_name,
            'LastName' : last_name,
            'StartDate': start_date,
            'Country': country,
            'DepartmentID': department_ID,
            'Title' : title,
            'ManagerID': manager_ID,
            'ManagerName': manager_name
            }
        )
    return response

def get_employee(id):
    response = EmployeesTable.get_item(
    Key={
        'EmployeeID': id
        }
    )
    print(response['Item'])
    return response['Item']

    
    


