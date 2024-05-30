## YT Videos

### Exam DP-900: Part 1: Real Exam Questions and Answers with Explanation | How to Pass DP-900
[Watch on YouTube](https://www.youtube.com/watch?v=U64NZ3DjsmI)

### 5 Types of Data Analytics:

1. **Descriptive Analytics**
    - Analyze historical data to identify patterns and trends
    - Answers the "What happened?" question

2. **Diagnostic Analytics**
    - Answers the "Why did it happen?" question
    - Understand the underlying reasons and market forces that caused patterns and trends
    - Root cause analysis

3. **Predictive Analytics**
    - Predict upcoming events and future trends
    - Relies on statistical algorithms
    - Answers the "What will happen?" question

4. **Prescriptive Analytics**
    - Provide suggestions and recommendations based on insights from predictive analytics and historical trends
    - Answers the "What actions should we take?" question while predictive analytics answers how to respond

5. **Cognitive Analytics**
    - Related to unstructured data like images, audio files, plain text, social media posts, etc.
    - Processes large amounts of unstructured data

### Data Processing Models

- **ETL (Extract, Transform, Load)**
    - Data is fully processed before being loaded to the target data store

- **ELT (Extract, Load, Transform)**
    - A powerful target data store transforms data after it is loaded

### Database Types

- **Relational Database**
    - High volumes of transactional writes
    - Strong consistency guarantees are required
    - Keys are used to enforce relationships between different tables

- **NoSQL Databases**
    - Classified into four types:
        1. **Key-Value Stores**
            - Simplest type of NoSQL
            - Key is unique and accepts only strings
            - Optimized for simple lookups
            - Examples: Azure Cache for Redis, Amazon DynamoDB

        2. **Document Stores**
            - Schema-free
            - Don't support relations; no relational integrity
            - Can query by attributes within a document
            - Handle a variety of data types and structures
            - Examples: Azure Cosmos DB, MongoDB

        3. **Column Family**
            - Organizes data by column rather than by row
            - Can handle large amounts of data and are often used for real-time big data applications
            - Examples: Apache Cassandra, Apache HBase

        4. **Graph Databases**
            - Natively support the analysis of relationships between entities
            - Data is represented as nodes and edges
            - Ideal for complex relationships
            - Examples: Azure Cosmos DB Graph API, Neo4j

### JSON Structure

1. **Root Object**: The initial value from the document
2. **Nested Object**: An attribute that contains multiple key-value pairs
3. **Nested Array**: An attribute containing a list of multiple values

### Exam DP-900: Part 2: Real Exam Questions and Answers with Explanation | How to Pass DP-900
[Watch on YouTube](https://www.youtube.com/watch?v=7ppGWK_RJPc&t=655s)

### Normalization
- Reduces data redundancy
- Improves data integrity
- Does not eliminate relationships between tables; it reinforces them

### Batch Processing
- Can output data to a file store, relational DB, NoSQL DB, or other data targets

### Platform as a Service (PaaS)
- Requires less setup and configuration than IaaS
- Does not provide administrators with the ability to control and update the operating system version
- Only IaaS services can be paused to reduce costs
- Provides built-in high availability
- Offers configuration scaling options
- Reduces administrative overhead for managing hardware

### Data Models

1. **Transaction Model**
    - Used in Online Transactional Processing (OLTP) systems
    - Designed to support high-speed transaction processing and ensure data integrity
    - Typically normalized to reduce redundancy and ensure ACID compliance

2. **Star Schema Model**
    - Consists of a fact table and dimension tables
    - Fact table contains quantitative data (facts) and foreign keys to related dimension tables
    - Dimension tables contain descriptive attributes

3. **Snowflake Model**
    - Dimension tables are normalized into multiple related tables
    - Reduces redundancy

### Database Components

1. **Dimension Table**
    - Contains descriptive attributes, such as customer or product
    - Provides context to the measures in a fact table
    - Used for filtering, grouping, and labeling data

2. **Fact Table**
    - Contains quantitative data
    - Central focus for analysis

3. **Bridge Table**
    - Used to connect many-to-many relationships between two tables

### SQL Table Components

- **Index**: A database object that helps improve the speed of data retrieval
- **View**: A database object whose content is defined by a query
- **Table**: A database object that holds data

### Azure Storage Types

- **Image Files**: Azure Blob Storage
- **Key/Value Pairs**: Azure Table Storage
- **Relationships Between Employees**: Azure Cosmos DB Gremlin API

### Azure SQL Database Security
- Protected by Azure Firewall
- Massively parallel processing (MPP) engine of Azure Synapse Analytics distributes processing across compute nodes

### Transparent Data Encryption (TDE)
- Encrypts SQL Server, Azure SQL Database, and Azure Synapse Analytics data files
- Encrypts sensitive data in a database and uses a certificate to protect the keys that encrypt the data

### Security Features

- **Authentication**: Supports Azure Active Directory (Azure AD) sign-ins to an Azure SQL Database
- **Firewall**: Prevents access to an Azure SQL Database from another network
- **Encryption**: Ensures that sensitive data never appears as plain text in an Azure SQL Database

### Exam DP-900: Part 3: Real Exam Questions and Answers with Explanation | How to Pass DP-900
[Watch on YouTube](https://www.youtube.com/watch?v=eU8_hX1yX08)

### Data Visualization Types

- **Scatter Plot**: Shows the relationship between two numerical values
- **Treemap**: Chart of colored, nested rectangles that displays individual data points represented by the size and color of a relative rectangle
- **Key Influencer**: Chart that displays the major contributors of a selected result or value

### Azure Data Factory Components

- **Dataset**: A representation of data structures within data stores
- **Linked Service**: Information used to connect to external resources
- **Pipeline**: A logical grouping of activities that performs a unit of work and can be scheduled

### File Storage

- **File Share**: Similar to Windows Explorer, where you can create folders and files

### Exam DP-900: Part 4: Real Exam Questions and Answers with Explanation | How to Pass DP-900
[Watch on YouTube](https://www.youtube.com/watch?v=GFurxlmLcCY)

### Multi-Factor Authentication

- Azure Active Directory (Azure AD) authentication to connect to an Azure SQL Database

### Microsoft SQL Server Data Tools (SSDT)
- Set of development tools for building SQL Server databases, Azure SQL databases, Analysis Services (AS) data models, Integration Services (IS) packages, and Reporting Services (RS) reports
- Graphical tool that supports project-oriented offline database development

### Exam DP-900: Part 5: Real Exam Questions and Answers with Explanation | How to Pass DP-900
[Watch on YouTube](https://www.youtube.com/watch?v=ZmxKHP_L0nk&ab_channel=TheTechBlackBoard)

### Azure SQL Managed Instance
- Native support for cross-database queries and transactions

### Trigger
- One of the ways to initiate pipeline execution

### Azure SQL Database
- Includes a fully managed backup service
- Has built-in high availability
- Uses Azure Advanced Threat Protection (ATP)
