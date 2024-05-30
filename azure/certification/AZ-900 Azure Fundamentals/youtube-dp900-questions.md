YT videos
Exam DP-900: Part 1: Real exam questions and answers with explanation| How to pass DP 900
https://www.youtube.com/watch?v=U64NZ3DjsmI

5 types of data analytics:

    1. Descriptive analytics
        - Analyze historical data to identify patterns and trends
        - Answer the "What happened?" question
    2. Diagnostic analytics
        - Answer the "why it happened?" question
        - Understand the underlying reasons and market forces that caused patterns and trends
        - Root cause analysis
    3. Predictive analytics
        - Predict upcoming events and future trends
        - Always relied on statistical algorithms
        - Answer "What will happen?" question
    4. Prescriptive analytics
        - Provide suggestions and recommendations based on the insights gleaned from predictive
            analytics and historial trends
        - Answer the "what actions should we take?" question while predictive answers how to respond
    5. Cognitive analytics
        - Related to unstructured data like images, audio files, plain text, social media posts, etc
        - Process large amounts of unstructured data

    ETL: Data is fully processed first before loaded to the target data store
    ELT: A target data store powerful enough to transform data after being loaded

    Relational database
        - High volumes of transactional writes
        - Strong consistency guarantees are required
        - Keys are used to enforce the relationships between different tables

    NoSQL can be classified into four types:
      1. Key-Value Stores
        - Simplest type of NoSQL
        - Key is unique and accepts only strings
        - Optimized to perform simple lookups
        - Azure Cache for Redis, Amazon DynamoDB
      2. Document Stores
        - Schema free
        - Don't support relations. No relational integrity
        - Can be used for all use cases of a Key Value. Additionaly, there's no limitation of querying just by the key but even the attributes within a document
        - Handle a wide variety of data types and structures
        - Azure Cosmos DB, MongoDB
      3. Column Family
        - Organizes data by column rather than by row
        - Can handle large amounts of data and are often used for real-time big data applications.
        - Apache Cassandra and Apache HBase
      4. Graph Databases
        - Natively support the analysis of relationships between entities
        - Data is represented as nodes and edges
        - Ideal for complex relationships
        - Azure Cosmos DB Graph API, Neo4j

      JSON structure:
        1. Root object: The initial value from the document
        2. Nested object: An attribute that contains multiple key-value values
        3. Nested array: An attribute containing a list of multiple values

Exam DP-900: Part 2: Real exam questions and answers with explanation| How to pass DP 900
https://www.youtube.com/watch?v=7ppGWK_RJPc&t=655s

  Normalization:
    - Reduce data redundancy
    - Improve data integrity
    - Doesn't eliminate relationships between tables. It does the opposite.

  Batch processing:
    - Can output data to a file store, relational db, NoSQL db, or any other data target

  Platform as a Service (PaaS):
    - Require less setup and configuration than IaaS database
    - Does not provide administrators with the ability to control and update the operating system version
    - Only IaaS services can be paused the service to reduce costs
    - Provide built-in high availability
    - Provide configuration scaling options
    - Reduce the administrative overhead for managing hardware

  Data models:
    1. Transaction Model:
      - Used in Online Transactional Processing (OLTP) systems
      - Designed to support high-speed transaction processing and ensure data integrity
      - Typically normalized to reduce redundancy and ensure ACID
    2. Star Schema Model:
      - Consist of a fact table and dimension tables
      - Fact table contains quantitative data (facts) and foreign keys to related dimension tables
      - Dimension tables contain descriptive attributes
    3. Snowflake Model:
      - Dimension tables are normalized into multiple related tables
      - Reduces redundancy

    1. Dimension Table:
      - Contain descriptive attributes, such as customer, product, etc.
      - Provide context to the measures in a fact table
      - Often used for filtering, grouping, labeling data
    2. Fact Table:
      - Contain quantitative data
      - Provide central focus for analysis
    3. Bridge:
      - Bridge table is used to connect many-to-many relationships between two tables

  SQL Table:
    - Index: A database object that helps improve the speed of data retrieval
    - View: A database object whose content is defined by a query
    - Table: A database object that holds data

  Image files > Azure Blob storage
  Key/value pairs > Azure Table storage
  Relationships between employees > Azure Cosmos DB Gremlin API

  Azure SQL Database is protected by Azure Firewall

  Massively parallel processing (MPP) engine of Azure Synapse Analytics distributes processing across compute nodes.
    - It does not control nodes. It actually computes nodes to process data

  Transparent Data Encryption (TDE):
    - Encrypt SQL Server, Azure SQL Database, and Azure Synapse Analytics data files
    - Encrypt sensitive data in a db and use a certificate to protect the keys that encrypt the data

  Authentication: Support Azure Active Directory (Azure AD) sign-ins to an Azure SQL Database
  Firewall: Prevent access to an Azure SQL database from another network
  Encryption: Ensure that sensitive data never appears as plain text in an Azure SQL database

Exam DP-900: Part 3: Real exam questions and answers with explanation| How to pass DP 900
https://www.youtube.com/watch?v=eU8_hX1yX08

    Scatter: A chart that shows the relationship between two numerical values
    Treemap: A chart of colored, nested rectangles that displays individual data points represented by the size and color of a relative rectangle
    Key influencer: A chart that displays the major contributors of a selected result of value

    Dataset: A representation of data structures within data stores
    Linked service: The information used to connect to external resources
    Pipeline: A logical grouping of activities that performs a unit of work and can be scheduled

    File share: Similar to windows explorer where I can create folders and files

Exam DP-900: Part 4: Real exam questions and answers with explanation| How to pass DP 900
https://www.youtube.com/watch?v=GFurxlmLcCY
