import os
from sqlalchemy import create_engine, MetaData

# Read environment variables
DATABASE_USER = os.getenv("DATABASE_USER", "docker")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "docker")
DATABASE_HOST = os.getenv("DATABASE_HOST", "db")
DATABASE_PORT = os.getenv("DATABASE_PORT", 5432)
DATABASE_DB = os.getenv("DATABASE_DB", "airbyte")

# Create the connection string
connection_string = f"jdbc:postgresql://{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DB}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)

# Connect to the database and retrieve the table names
def get_tables(engine):
    try:
        # Reflect the metadata
        metadata = MetaData()
        metadata.reflect(bind=engine)
        
        # Get table names
        tables = metadata.tables.keys()
        return tables
    except Exception as error:
        print(f"Error retrieving tables: {error}")
        return []

def main():
    try:
        # Get tables
        tables = get_tables(engine)
        
        # Print table names
        if tables:
            print("Available tables:")
            for table in tables:
                print(table)
        else:
            print("No tables found.")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
