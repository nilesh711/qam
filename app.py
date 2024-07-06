from flask import Flask, render_template
import pyodbc
import pandas as pd

app = Flask(__name__)

def fetch_data_from_azure_sql():
    server = ''
    =''
    username = ''
    password = ''
    driver= '{ODBC Driver 18 for SQL Server}' 
    try:
        conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        cursor.execute('SELECT TOP(20) * FROM [SalesLT].[Customer];')  
        rows = cursor.fetchall()
        columns = [column[0] for column in  cursor.description]
        dt = []
        for row in rows:
            temp= []
            for ele in row:
                temp.append(ele)
            dt.append(temp)
        
        df = pd.DataFrame(dt, columns =columns)
        return df
    except pyodbc.Error as e:
        print('Error connecting to Azure SQL Database:', e)


@app.route('/')
def index():
    df = fetch_data_from_azure_sql()  
    return render_template('index.html', df=df)

@app.route('/task2')
def task2():
    df = fetch_data_from_azure_sql()  
    return render_template('task2.html', df=df)

@app.route('/task3')
def task3():
    df = fetch_data_from_azure_sql()  
    return render_template('task3.html', df=df)

if __name__ == '__main__':
    app.run(debug=True)