# Explore Core Data Concepts

## [Unit 1: Introduction](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/?WT.mc_id=cloudskillschallenge_be6235e5-c168-4993-b1bb-e53bade5ddee)
- Identify common data formats
- Describe options for storing data in files
- Describe options for storing data in databases
- Describe characteristics of transactional data processing solutions
- Describe characteristics of analytical data processing solutions

## [Unit 2: Identify data formats](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/2-data-formats)

- Data is a collection of facts.
- Entities represent important data to an organization.
- Each entity has one or more attributes. E.g., Customer table has name, address, etc.

### Data is classified as structured, semi-structured, or unstructured.

1. **Structured Data**
    - Fixed schema: All the data has the same fields or properties.
    - Tabular: Normally the structured schema.
    - Data is often stored in a database with multiple tables linked by key values in a relational model.

2. **Semi-structured Data**
    - Flexible schema: Has some structure, but allows variation. E.g., some customers may have multiple phone numbers and none at all.
    - JSON format: Commonly used.

3. **Unstructured Data**
    - Data doesn't follow a pattern.
    - Documents, images, audio, video data are examples of an unstructured format.

## [Unit 3: Explore file storage](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/3-file-storage)

### Common file formats

1. **Delimited text files**
    - The most common format
    - Usually separated by commas
    - Good choice for structured data

2. **JSON**
    - Define multiple attributes
    - Good for structured and semi-structured data

3. **XML**
    - Human-readable data popular in the 90s and 2000s

4. **Binary Large Object (BLOB)**
    - Stored in binary mode (1's and 0's)
    - Contains images, video, audio, and application-specific documents.

5. **Optimized file formats**
    - **Avro:**
        - Row-based format
        - Created by Apache
        - Each record contains a header that describes the structure of the data
        - Header is stored as JSON while the data is binary information
        - The application uses the info in the header to parse the binary data
        - Good format for compressing data and minimizing storage
    - **ORC (Optimized Row Columnar format):**
        - Organizes data into columns rather than rows
        - Developed by HortonWorks
        - Optimized for reading and writing operations in Apache Hive
        - The file contains stripes of data which hold the data for a column or set of columns
        - A stripe contains an index into the rows
    - **Parquet:**
        - Another columnar data format
        - Made by Cloudera and Twitter
        - Contains row groups
        - Includes metadata
        - Applications use the metadata to quickly find the correct chunk of rows
        - Specialized in storing and processing nested data efficiently
        - Supports very efficient compression and encoding schemes

## [Unit 4: Explore databases](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/4-databases)

A database is a central system that stores data and is accessed by queries.

1. **Relational databases**
    - Used to store structured data.
    - Entities hold the stored data.
    - Primary key (PK) uniquely identifies each instance of an entity.
    - Normalized data.

2. **Non-relational databases**
    - Don't apply a relational schema to the data.
    - Four types of non-relational databases:
        1. **Key-value db:** Consists of a unique key and an associated value. The value can be anything.
        2. **Document db:** A specific form of key-value db. The value is a JSON document.
        3. **Column family db:** Tabular data, but columns can be divided into groups known as column-families.
        4. **Graph db:** Stores entities as nodes with links to define relationships between them.

## [Unit 5: Explore transactional data processing](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/5-transactional-data-processing)

Transactional systems record transactions which are specific events.
- High volume of data and needs to be accessible very quickly.
- Often referred to as Online Transactional Processing (OLTP).

### OLTP relies on databases that are good for both reading and writing.
- Always associated with CRUD operations.
- OLTP enforces transactions on ACID semantics:
    1. **Atomicity:** Each transaction is treated as a single unit, which succeeds or fails completely.
    2. **Consistency:** Can only take the data in the database from one valid state to another.
    3. **Isolation:** Concurrent transactions cannot interfere with one another. Must result in a consistent state.
    4. **Durability:** When a transaction has been committed, it'll remain committed.

OLTP systems are typically used to support live applications that process business data, often referred to as line of business (LOB) applications.

## [Unit 6: Explore analytical data processing](https://learn.microsoft.com/en-us/training/modules/explore-core-data-concepts/6-analytical-processing)

Analytical data typically uses read-only (or mostly read-only) systems.
- Always related to vast volumes of historical data or business metrics.

1. **Data lakes:** Common in large-scale data analytical processing scenarios.
2. **Data warehouse:** Stores data in a relational schema optimized for read operations.
3. **Data Lakehouses:** Combine the flexible and scalable storage of a data lake with the relational querying semantics of a data warehouse.
