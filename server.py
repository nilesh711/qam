from flask import Flask, render_template
import pypyodbc as odbc
import pandas as pd
from databaseInfo import username, password, server, database
 
 
connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:'+server+',1433;Database='+database+';Uid='+username+';Pwd='+password+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
conn = odbc.connect(connection_string)
 
app = Flask(__name__)
 
 
sql = '''SELECT TOP(20) * FROM [SalesLT].[Customer];'''
sql1 = '''SELECT TOP (20) p.Name, p.Color, p.Size, p.Weight FROM [SalesLT].[Product] AS p INNER JOIN [SalesLT].[ProductCategory] AS pc ON p.ProductCategoryID = pc.ProductCategoryID;'''
def task1Table(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
 
    dataset = cursor.fetchall()
 
    columns = [column[0] for column in  cursor.description]
    df = pd.DataFrame(dataset, columns = columns)
    return df
 
# cursor1 = conn.cursor()
# cursor1.execute(sql1)
 
# dataset1 = cursor1.fetchall()
# columns1 = [column[0] for column in  cursor1.description]
# df1 = pd.DataFrame(dataset1, columns = columns1)
# print(df1)
 
 
@app.route("/")
def task():
    container = ['static/image/img1.jpg','static/image/img2.jpg','static/image/img3.jpg']
    return render_template('index.html', container=container)
    # return "<p>Hello, World!</p>"
 
# @app.route("/task1")
# def task1():
#     container = ['static/image/img1.jpg','static/image/img2.jpg','static/image/img3.jpg']
#     return render_template('index.html', container=container)
 
@app.route("/task2")
def task2():
    df = task1Table(sql)
    user = df.to_html(classes='table table-striped', index=False)
    # user = [user , df]
    context = {
        'user' : user,
        'df':df
    }
    # print(df)
    # return render_template('task2.html', users=user)
    return render_template('task2.html', **context)
    # return "<p>Hello, World!</p>"
 
@app.route("/task3")
def task3():
    df = task1Table(sql1)
    user = df.to_html(classes='table table-striped', index=False)
    # user = [user , df]
    context = {
        'user' : user,
        'df':df
    }
    print(df)
    return render_template('task3.html', **context)
    # return "<p>Hello, World!</p>"
 
if __name__ == "__main__":
    app.run(debug=True)
 


