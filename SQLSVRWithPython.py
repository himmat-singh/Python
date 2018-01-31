#import pypyodbc
import pypyodbc

#import pprint
import pprint

#create connection
connection = pypyodbc.connect('Driver={SQL Server};' 'Server=serverip/dns;' 'Database=dbname;' 'uid=user;pwd=password')

#create cursor
cursor = connection.cursor()

#create SQL command
sqlCommand = ("SELECT * FROM TABLE WHERE COLUMN = ?")

#pass parameters values
values = [3]

#execute sql command
cursor.execute(sqlCommand,values)

#obtained resultset
results = cursor.fetchone()

#to print obtained results
pprint.pprint(results)

