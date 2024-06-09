import pyodbc

# Spin up a docker with sqlserver
# docker run --platform linux/amd64 -e 'ACCEPT_EULA=Y' -e 'MSSQL_SA_PASSWORD=admin@12345' -p 1433:1433 --name sql_server -d mcr.microsoft.com/mssql/server:2022-latest

# Define the connection parameters
server = 'localhost,1433'
database = 'master'
username = 'sa'
password = 'admin@12345'

# Create a connection string
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};TrustServerCertificate=yes;'

# Establish the connection
try:
    connection = pyodbc.connect(connection_string)
    print("Connection successful")

    # Create a cursor object using the connection
    cursor = connection.cursor()

    # Create the table dbo.teamStructure
    create_table_query = """
    CREATE TABLE dbo.teamStructure (
        idTeam INT PRIMARY KEY,
        nameTeam VARCHAR(255) NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("Table dbo.teamStructure created successfully")

    # Insert values into the dbo.teamStructure table
    insert_values_query = """
    INSERT INTO dbo.teamStructure (idTeam, nameTeam) VALUES
    (1, 'Actuarial Team'),
    (2, 'Pricing Team'),
    (3, 'Underwriting Team');
    """
    cursor.execute(insert_values_query)
    connection.commit()
    print("Values inserted into dbo.teamStructure successfully")

    # Execute a query to verify the insert
    cursor.execute("SELECT * FROM dbo.teamStructure;")
    
    # Fetch and display the results
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    # Close the connection
    connection.close()

except Exception as e:
    print(f"Error: {e}")