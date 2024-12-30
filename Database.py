import pyodbc

def create_connection():
    server = 'MSI'
    database = 'HEPAS'
    username = 'MSI'
    password = ''
    driver = 'ODBC Driver 17 for SQL Server'

    connection_string = f"DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={username};PWD={password};TRUSTED_CONNECTION=YES;"

    try:
        connection = pyodbc.connect(connection_string)
        print("Connected to db!")
        return connection
    except Exception as e:
        print(f"Error: {str(e)}")
        return None