import sqlite3 as sql

def insertUser(name,phone_number,password,age,gender,relationship_status):
    msg=False
    try:   
        con = sql.connect("databases/loan_db.sqlite")
        cur = con.cursor()
        cur.execute("INSERT INTO users (phone_number,password) VALUES (?,?)", (phone_number,password))
        cur.execute("INSERT INTO Loan_Table (NAME,AGE,GENDER,RELATIONSHIP_STATUS) VALUES (?,?,?,?)", (name,age,gender,relationship_status))
        con.commit()
        msg=True
    except:
        con.rollback()
        msg=False
    finally:
        con.close()
        return msg


def retrieveUsers(phone_number,password):
    con = sql.connect("databases/loan_db.sqlite")
    cur = con.cursor()
    cur.execute("SELECT * FROM users where phone_number=? and password = ?" ,(phone_number,password))
    users = cur.fetchall()
    result = False
    if len(users) == 1:
        result = True
    con.close()
    return result