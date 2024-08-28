
def getuserdetails(username,password,con):
    cur = con.cursor()
    cur.execute("select * from users where username=%s and password=%s",[username,password])
    emp_details=cur.fetchall()
    return emp_details


def getstudentsdetails(department_id,class_name,con):
    cur = con.cursor()
    cur.execute("select s.id,s.full_name,s.class_name.s.department_id,c.id from students s join courses c on c.department_id=s.department_id and c.class=s.class\
        where c.department_id=%s and c.class=%s",[department_id,class_name])
    students_details=cur.fetchall()
    return students_details

def attendence(student_id,course_id,present,submitted_by,updated_at,con):
    cur = con.cursor()
    cur.execute("insert into attendance_log(student_id,course_id,present,submitted_by,updated_at)\
                values(%s,%s,%s,%s,%s)",[student_id,course_id,present,submitted_by,updated_at])
    
    return "attenence submitted"

def updateattendencedetails(student_id,course_id,present,submitted_by,updated_at,con):
    cur = con.cursor()
    cur.execute("update attendance_log set present=%s where student_id=%s and course_id=%s and submitted_by=%s\
               and updated_at=%s ",[present,student_id,course_id,submitted_by,updated_at])
    
    return "Attendance updated successfully"