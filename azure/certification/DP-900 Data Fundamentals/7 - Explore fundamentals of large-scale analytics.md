# Explore Fundamentals of Large-Scale Analytics

## [Unit 1: Introduction](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/)

- Identify common elements of a large-scale data analytics solution
- Describe key features for data ingestion pipelines
- Identify common types of analytical data store
- Identify platform-as-a-service (PaaS) analytics services in Azure
- Provision Azure Synapse Analytics and use it to ingest, process, and query data
- Describe features of Microsoft Fabric - a software-as-a-service (SaaS) solution for data analytics
- Use Microsoft Fabric to ingest and analyze data

## [Unit 2: Describe Data Warehousing Architecture](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/2-describe-warehousing)

The architecture typically includes:
1. Data ingestion and processing: ETL/ELT resulting in optimized data for analytical queries. Batch processing or Real-time processing.
2. Analytical data store: Data Warehouse and Data lakes.
3. Analytical data model: Cube format which aggregates data.
4. Data visualization: Reports, dashboards, etc.

## [Unit 3: Explore Data Ingestion Pipelines](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/3-data-ingestion-pipelines)

Creation of pipelines that orchestrate ETL processes using tools like Azure Data Factory, Azure Synapse Analytics, or Microsoft Fabric.

## [Unit 4: Explore Analytical Data Stores](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4-analytical-data-stores)

### Data Warehouses:
- Relational databases optimized for data analytics.
- Data is transformed into a schema (Star or snowflake schema).
- Suitable for structured transactional data.

### Data Lakehouses:
- File-based storage, often using Hadoop or Spark.
- Schema-on-read approach for defining tabular schemas on semi-structured data files.
- Suitable for structured, semi-structured, and unstructured data.

## [Unit 5: Explore Platform-as-a-Service (PaaS) Solutions](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/4b-platform-services)

Three main PaaS services:
1. Azure Synapse Analytics: End-to-end solution for large-scale data analytics.
2. Azure Databricks: Data analytics solution built on Apache Spark.
3. Azure HDInsight: Supports multiple open-source data analytics cluster types.

## [Unit 7: Explore Microsoft Fabric](https://learn.microsoft.com/en-us/training/modules/examine-components-of-modern-data-warehouse/5b-fabric)

SaaS solution offering data storage and analysis capabilities.
