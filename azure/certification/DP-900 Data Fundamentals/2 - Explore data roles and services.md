# Explore Data Roles and Services

## [Unit 1: Introduction](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/?WT.mc_id=cloudskillschallenge_be6235e5-c168-4993-b1bb-e53bade5ddee)
- Identify common data professional roles
- Identify common cloud services used by data professionals

## [Unit 2: Explore job roles in the world of data](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/2-explore-job-roles)

### Three key job roles:
1. **Database Administrators:** Manage databases, assign permissions, store and restore backup copies.
2. **Data Engineers:** Manage infrastructure, process data across the organization, apply cleaning routines, identify data governance rules, implement pipelines to move and transform data between systems.
3. **Data Analysts:** Explore and analyze data to create visualizations and charts.

## [Unit 3: Identify data services](https://learn.microsoft.com/en-us/training/modules/explore-roles-responsibilities-world-of-data/3-data-services)

### Azure SQL
Collective name for a family of relational database solutions:
1. **Azure SQL Database:** Fully managed PaaS database.
2. **Azure SQL Managed Instance:** Instance of the SQL Server. More administrative responsibility.
3. **Azure SQL VM:** Virtual machine with an installation of SQL Server.

- **Database Administrators** typically provision and manage Azure SQL database systems to support line of business (LOB) applications.
- **Data Engineers** use SQL database systems for creating pipelines to perform ETL operations.
- **Data Analysts** query SQL databases directly to create reports and dashboards for analytical purposes.

- **Azure SQL Database:** Serverless platform as a service (PaaS) SQL instance.
- **SQL Managed Instance:** PaaS service, databases maintained in the same SQL Managed Instance cluster.
- **SQL Server on Azure VMs:** Running Windows or Linux, not serverless.

- **SQL Managed Instance:** Allows migration of an entire SQL server to the cloud without requiring management of the infrastructure post-migration.
- **SQL Server on Azure VMs:** Requires management of all aspects.
- **Azure SQL Database:** Supports most, but not all, core database-level capabilities of SQL Server.

### Azure Database for Open-Source Relational Databases
Includes managed services for popular open-source databases:
1. **Azure Database for MySQL:** Commonly used in Linux, Apache, MySQL, and PHP stack applications.
2. **Azure Database for MariaDB**
3. **Azure Database for PostgreSQL**

### Azure Cosmos DB
- NoSQL database.

### Azure Storage
Core Azure service:
1. **Blob containers:** Scalable, cost-effective storage for binary files.
2. **File shares:** Network file shares.
3. **Tables:** Key-value storage.

### Azure Data Factory
- Enables creation and scheduling of pipelines for ETL operations.

### Azure Synapse Analytics
PaaS service for analytical purposes:
1. **Pipelines:** Same technology as ADF.
2. **SQL:** Highly scalable SQL database engine, optimized for data warehouse workloads.
3. **Apache Spark:** Open-source distributed data processing system.
4. **Azure Synapse Data Explorer:** High-performance data analytics solution for real-time querying of log and telemetry data using Kusto Query Language (KQL).

### Azure Databricks
- Azure-integrated version of Databricks:
  - Combines Apache Spark with SQL database semantics for large-scale data analytics.
  - **Data Engineers** create analytical data.
  - **Data Analysts** use native notebooks to query and visualize data.

### Azure HDInsight
Service providing Azure-hosted clusters for popular Apache solutions:
1. **Apache Spark**
2. **Apache Hadoop:** MapReduce
3. **Apache HBase:** NoSQL solution
4. **Apache Kafka:** Message broker

### Azure Stream Analytics
- Real-time stream processing engine.

### Azure Data Explorer
- Standalone service offering the same solution as Azure Synapse Data Explorer.

### Microsoft Purview
- Service for data governance and discoverability.

### Microsoft Fabric
SaaS analytics platform:
1. **Data ingestion and ETL**
2. **Data lakehouse analytics**
3. **Data warehouse analytics**
4. **Data Science and machine learning**
5. **Real-time analytics**
6. **Data visualization**
7. **Data governance and management**
