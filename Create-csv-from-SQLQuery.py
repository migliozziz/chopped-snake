import csv
import pyodbc

def add_jobName(results):
    for row in results:
        rawJobName = row[0]
        jobNameList = rawJobName.split('.')
        realJobName = jobNameList[0]
        queue   = row[1]
        entry = [realJobName, queue]
        writer = csv.writer(open("JobListing.csv", "ab"), delimiter=',',
                            dialect='excel')
        writer.writerow(entry)
    return

# Open DB connection
db = pyodbc.connect('DRIVER={SQL SERVER};SERVER=;\
                    DATABASE=;UID=;PWD=')

# Prepare a cursor object using cursor() method
cursor = db.cursor()

# SQL Query
sql =  ""

try:
    # Execute SQL command
    cursor.execute(sql)
    # Fetch all the rows
    results = cursor.fetchall()
    for row in results:
        rawJobName = row[0]
        jobNameList = rawJobName.split('.')
        realJobName = jobNameList[0]
        queue   = row[1]
        print "Jobname: %s\t\t%s" % (realJobName, queue)
        
except:
    print "Error: Unable to fetch data."

# Disconnect from server
db.close()
add_jobName(results)


    
    
