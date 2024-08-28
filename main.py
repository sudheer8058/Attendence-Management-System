from flask import Flask, request
import psycopg2 as p
import func as f


app = Flask(__name__)
con=p.connect("dbname='test' user='test@123'")


@app.route('/userLogin',methods=["POST"])
def userlogin():
    input_data = request.json
    username = input_data['username']
    password = input_data['password']
    res = f.getuserdetails(username,password,con)
    message = "user not authorized"
    if len(res):
        message = "login successfully"
    return message

@app.route('/getStudentInfo',methods=["GET"])
def getStudentInfo():
    input_data = request.json
    department_id = input_data['department_id']
    class_name = input_data['class_name']
    
    studetnts_data = f.getstudentsdetails(department_id,class_name,con)
    return studetnts_data

@app.route('/attendance',methods=["POST"])
def attendance():
    input_data = request.json
    student_id = input_data['student_id']
    course_id = input_data['course_id']
    present = input_data['present']
    submitted_by = input_data['submitted_by']
    updated_at = input_data['updated_at']
    
    studetnts_data = f.attendence(student_id,course_id,present,submitted_by,updated_at)
    return "Attendance Submitted successfully"

@app.route('/updateAttendance',methods=["POST"])
def updateAttendance():
    input_data = request.json
    student_id = input_data['student_id']
    course_id = input_data['course_id']
    present = input_data['present']
    submitted_by = input_data['submitted_by']
    updated_at = input_data['updated_at']
    
    studetnts_data = f.updateattendencedetails(student_id,course_id,present,submitted_by,updated_at)
    return "Attendance updated successfully"

if __name__ == "__main__":
    app.run(debug=True)