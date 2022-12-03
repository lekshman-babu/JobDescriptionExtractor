import sqlite3 as sq

#connecting to a database
connect=sq.connect("job")

#creating a database
cursor=connect.cursor()

#drop a table
def drop():
    cursor.execute("""DROP TABLE job_details""")
    connect.commit()


#create a table
def create():
    cursor.execute("""CREATE TABLE job_details(
        "job_name" TEXT,
        "skills_req" TEXT
    ) """)
    connect.commit()

#insert jobs
def insert(jobskill):
    cursor.execute("""INSERT INTO job_details VALUES(?,?)""",jobskill)
    connect.commit()
            
#display jobs
def select():
    cursor.execute("""SELECT * FROM job_details""")
    storedjob=cursor.fetchall()
    connect.commit()
    return storedjob
