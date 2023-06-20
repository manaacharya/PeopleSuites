import aws_controller
import os
from flask import Flask, render_template, request, redirect, send_file, jsonify
import boto3

UPLOAD_FOLDER = "uploads"
BUCKET = "lab7-images-data"
s3 = boto3.client('s3')

app = Flask(__name__)

@app.route('/test')
def test():
    print("Yay! Test Sucessful!")
    return 'TEST SUCESSFUL'

@app.route('/')
def index():
    return "Employees API"
    
@app.route('/peoplesuite/apis/employees/')
def get_employees():
    return jsonify(aws_controller.get_employees())
    
@app.route('/peoplesuite/apis/employees/<employee_id>/profile')
def get_employee(employee_id):
    return jsonify(aws_controller.get_employee(employee_id))

@app.route('/peoplesuite/apis/employees/<employee_id>/photo')
def get_employee_picture(employee_id):
    return aws_controller.get_employee_picture(employee_id)
    
@app.route('/peoplesuite/apis/employees//photo/upload')
def upload_page():
    return render_template('upload.html')

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, secure_filename(f.filename)))
        aws_controller.upload_file(f"uploads/{f.filename}", BUCKET)
        return redirect("/")
    
if __name__ == '__main__':
    app.run()
