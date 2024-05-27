# Explore Fundamental Relational Data Concepts

## [Unit 1: Introduction](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/?WT.mc_id=cloudskillschallenge_be6235e5-c168-4993-b1bb-e53bade5ddee)
- Identify characteristics of relational data
- Define normalization
- Identify types of SQL statements
- Identify common relational database objects

## [Unit 2: Understand Relational Data](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/2-understand-relational-data)

- Relational tables are a format for structured data.

## [Unit 3: Understand Normalization](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/3-normalization)

- Normalization is the process that minimizes data duplication and enforces data integrity.

### Simple Definition for Normal Forms (Fn's):
1. Separate each entity into its own table.
2. Separate each discrete attribute into its own column.
3. Uniquely identify each entity instance (row) using a primary key.
4. Use foreign key columns to link related entities.

## [Unit 4: Explore SQL](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/4-query-with-sql)

- SQL: Structured Query Language.

### SQL Statement Types:
1. **Data Definition Language (DDL)**
   - Used to create, modify, and remove tables and other objects in a database.
   - Statements:
     - **Create:** Create a new object in the database.
     - **Alter:** Modify the structure of an object.
     - **Drop:** Remove an object from the database.
     - **Rename:** Rename an existing object.
2. **Data Control Language (DCL)**
   - Used to manage access to objects in a database.
   - Statements:
     - **Grant:** Grant permission to perform specific actions.
     - **Deny:** Deny permission to perform specific actions.
     - **Revoke:** Remove a previously granted permission.
3. **Data Manipulation Language (DML)**
   - Used to manipulate the rows in tables.
   - Statements:
     - **Select:** Read rows from a table.
     - **Insert:** Insert new rows into a table.
     - **Update:** Modify data in existing rows.
     - **Delete:** Delete existing rows.

## [Unit 5: Describe Database Objects](https://learn.microsoft.com/en-us/training/modules/explore-relational-data-offerings/5-database-objects)

### Common Database Objects:
- **View:** Virtual table based on the results of a SELECT query.
- **Stored Procedure:** SQL statements that will run on a command. Used to encapsulate programmatic logic.
- **Index:** Helps to search for data in a table.
