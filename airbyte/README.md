What is Airbyte

Open-source data integration tool that moves data from one system to another

Benefits
    - Open-source
    - User Interface
    - Scalable
    - Extensible

Core components
    - Airbyte DB (Config DB): Stores all the connection metadata (credentials, frequency, etc)
    - Airbyte WebApp: Airbyte's user interface (port 8000)
    - Airbyte Server (API): Airbyte's API to create and manage resources
    - Temporal (Scheduler): Schedule jobs (sync, check, discover, etc)
    - Airbyte Worker: Pull jobs from a queue and execute them

Not useful
    - Streaming: Sometimes Airbyte has low latency

How the transfer works
    - After syncing, which means the action of transferring the source data to the destination
    While airbyte is transferring it, it creates a temp object called raw__stream_<stream_name>
    - In this object we'll have:
        - _airbyte_raw_id: Unique row identifier
        - _airbyte_extracted_at: When the data was ingested
        - _airbyte_loaded_at: When the data was loaded into the destination
        - _airbyte_meta: Contains the metadata
        - _airbyte_data: Contains a given record
    Finally, airbyte creates the final table with the <stream_name> name where will contain the data transferred

What is classification
    - Tell the e
docker compose -f airbyte-docker-compose.yml up -d