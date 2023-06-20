from flask import Flask, jsonify
import aws_controller

app = Flask(__name__)

@app.route('/test')
def test():
    print("Yay! Test Sucessful!")
    return 'TEST SUCESSFUL'

@app.route('/')
def index():
    return "Department API"

@app.route('/peoplesuite/apis/departments')
def get_departments():
    return jsonify(aws_controller.get_departments())

@app.route('/peoplesuite/apis/departments/<department_id>')
def get_department(department_id):
    return jsonify(aws_controller.get_department(department_id))

@app.route('/peoplesuite/apis/departments/<department_id>/employees')
def get_employees_from_department(department_id):
    return jsonify(aws_controller.get_employee_from_department(department_id))
        
if __name__ == '__main__':
    app.run()
