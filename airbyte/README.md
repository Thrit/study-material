## What is Airbyte

Open-source data integration tool that moves data from one system to another

### Benefits
- Open-source
- User Interface
- Scalable
- Extensible

### Core components
- **Airbyte DB (Config DB)**: Stores all the connection metadata (credentials, frequency, etc)
- **Airbyte WebApp**: Airbyte's user interface (port 8000)
- **Airbyte Server (API)**: Airbyte's API to create and manage resources
- **Temporal (Scheduler)**: Schedule jobs (sync, check, discover, etc)
- **Airbyte Worker**: Pull jobs from a queue and execute them

### Not useful
- Streaming: Sometimes Airbyte has low latency

### How the transfer works
- After syncing, which means the action of transferring the source data to the destination, while Airbyte is transferring it, it creates a temp object called `raw__stream_<stream_name>`
  - In this object we'll have:
    - `_airbyte_raw_id`: Unique row identifier
    - `_airbyte_extracted_at`: When the data was ingested
    - `_airbyte_loaded_at`: When the data was loaded into the destination
    - `_airbyte_meta`: Contains the metadata
    - `_airbyte_data`: Contains a given record
- Finally, Airbyte creates the final table with the `<stream_name>` name where the data transferred will be contained

## Sync modes
`<name_1> | <name_2>`

`<name_1>`: How Airbyte reads data from the source
`<name_2>`: How Airbyte writes data into the destination

### Incremental | Append + Deduplicated
- **Standard**:
  - Pros:
    - Efficient for high frequency syncs
    - Stores history
    - De-duplicates final data
  - Cons:
    - Primary key required
    - A suitable cursor must be available
    - Deletes are not detected
    - Intermediate states not captured
- **CDC**:
  - Pros:
    - Efficient for high frequency syncs
    - Stores history
    - Deletes are handled
    - Intermediate states captured
    - De-duplicates final data
    - No cursor field is required
  - Cons:
    - Primary key required
    - Not available for all sources
    - Requires access to the transaction log

### Full refresh | Overwrite
- **Standard**:
  - Pros:
    - Deletes are handled
    - Good for small data volume
    - Final data does not have duplicates
  - Cons:
    - No history is stored
    - Inefficient for large data
    - Inefficient for high frequency syncs
- **CDC**:
  - Pros:
    - Same as Standard
  - Cons:
    - Same as Standard

### Incremental | Append
- **Standard**:
  - Pros:
    - Efficient for high frequency syncs
    - Stores history
    - Primary key not required
  - Cons:
    - A suitable cursor must be available
    - Final data may contain duplicates
    - Deletes are not detected
    - Intermediate states not captured
- **CDC**:
  - Pros:
    - Efficient for high frequency syncs
    - Stores history
    - Deletes are transmitted and logged
    - Intermediate states captured
    - No cursor field is required
  - Cons:
    - Primary key required
    - Final data may contain duplicates
    - Not available for all sources
    - Requires access to the transaction log

### Full refresh | Append
- **Standard**:
  - Pros:
    - Store history
    - Good for small data volume
  - Cons:
    - Storage may explode
    - Inefficient for large data
    - Inefficient for high frequency syncs
    - Final data will contain duplicates
- **CDC**:
  - Pros:
    - Same as Standard
  - Cons:
    - Same as Standard

## Schema replication
- **Detect changes and manually approve**:
  - Schema changes will be detected but not propagated. Schema will run with the previous setup
- **Detect changes and pause connection**:
  - Schema will be automatically disabled as soon as any schema changes are detected
- **Propagate field changes only**:
  - Only columns changes will be propagated
- **Propagate all field and stream changes**:
  - All new tables and column changes from the source will automatically be propagated and reflected in the destination

## Change Data Capture (CDC)
Software architecture pattern that allows tracking changes in real-time or not made to a database and react

### Limitations:
- CDC incremental is only supported for tables with PK
- Data must be in tables, not views
- The modifications you are trying to capture must be made using DELETE/INSERT/UPDATE. Changes made from TRUNCATE/ALTER don't appear in logs
- No support on schema changes automatically for CDC sources. Recommended resetting and resyncing data if any schema changes are made
- There are database-specific limitations
- The records produced by DELETE statements only contain PK. All other data fields are unset

    - docker compose -f airbyte-docker-compose.yml up -d