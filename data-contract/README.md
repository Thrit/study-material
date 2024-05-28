### Data Contracts

Data contracts refer to arrangements which are officially agreed upon to state the sequence, design and regulations to which data is exchanged among different systems or entities, in order to help keep its integrity, reliability, and validity by fostering good flow of information across diverse platforms or applications.

### Installing and Using DataContracts.com for Standard Tests

To install and run tests using DataContracts.com, follow these steps:

1. Install the DataContract CLI using pip:
    ```bash
    pip install datacontract-cli
    ```

2. Usage:
    ```bash
    # create a new data contract from example and write it to datacontract.yaml
    $ datacontract init datacontract.yaml

    # lint the datacontract.yaml
    $ datacontract lint datacontract.yaml

    # execute schema and quality checks
    $ datacontract test datacontract.yaml

    # execute schema and quality checks on the examples within the contract
    $ datacontract test --examples datacontract.yaml

    # export data contract as html (other formats: avro, dbt, dbt-sources, dbt-staging-sql, jsonschema, odcs, rdf, sql, sodacl, terraform, ...)
    $ datacontract export --format html datacontract.yaml > datacontract.html

    # import avro (other formats: sql, glue, bigquery...)
    $ datacontract import --format avro --source avro_schema.avsc

    # find differences between to data contracts
    $ datacontract diff datacontract-v1.yaml datacontract-v2.yaml

    # find differences between to data contracts categorized into error, warning, and info.
    $ datacontract changelog datacontract-v1.yaml datacontract-v2.yaml

    # fail pipeline on breaking changes. Uses changelog internally and showing only error and warning.
    $ datacontract breaking datacontract-v1.yaml datacontract-v2.yaml
    ```
