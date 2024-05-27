# Explore Azure Storage for Non-Relational Data

## [Unit 1: Introduction](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/1-introduction)
- Describe features and capabilities of Azure Blob Storage
- Describe features and capabilities of Azure Data Lake Gen2
- Describe features and capabilities of Azure File Storage
- Describe features and capabilities of Azure Table Storage
- Provision and use an Azure Storage account

## [Unit 2: Explore Azure Blob Storage](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/2-azure-blob-storage)

Azure Blob Storage stores massive amounts of unstructured data as binary large objects (Blobs). Blobs are stored in containers and support three different types:

1. **Block Blobs**
   - Composed of a set of blocks, each varying in size up to 4000 MiB.
   - Best used to store discrete, large, binary objects that change infrequently.

2. **Page Blobs**
   - Organized as a collection of fixed-size 512-byte pages.
   - Used for virtual disk storage for VMs, enabling random access and used for VHDs.

3. **Append Blobs**
   - Optimized for append operations. Updating and deleting existing blocks is not supported.
   - Maximum size is 195GB.

Blob storage provides three access tiers:

1. **Hot Tier**: Frequently accessed data.
2. **Cool Tier**: Infrequently accessed data.
3. **Archive Tier**: Lowest storage cost, ideal for storing historical data.

You can create lifecycle management policies to move data through these tiers.

## [Unit 3: Explore Azure Data Lake Storage Gen2](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/3-azure-data-lake-gen2)

- **Azure Data Lake Storage Gen1**: Separate service for hierarchical data storage for analytical data lakes.
- **Azure Data Lake Storage Gen2**: New version integrated into Azure Storage, providing hierarchical namespace.

To enable Azure Data Lake Storage Gen2, you must enable the Hierarchical Namespace, which cannot be reverted once changed.

## [Unit 4: Explore Azure Files](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/4-azure-files)

Azure Files provides cloud-based network shares, eliminating hardware costs and maintenance overhead, and offering high availability and scalable cloud storage for files.

- Maximum size of a single file is 1TB.
- Supports up to 2000 concurrent connections per shared file.

Azure File Storage offers two performance tiers:

1. **Standard Tier**: Uses hard disk-based hardware in a data center.
2. **Premium Tier**: Uses solid-state disks.

Azure Files supports two common network file sharing protocols:

1. **Server Message Block (SMB)**: Used across multiple operating systems (Windows, Linux, macOS).
2. **Network File System (NFS)**: Used by some Linux and macOS versions. Must use the premium tier.

## [Unit 5: Explore Azure Tables](https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-non-relational-data-services-azure/5-azure-tables)

Azure Table Storage is a NoSQL solution that makes use of tables containing key/value pairs.

- Suitable for storing semi-structured data.
- All rows must have a unique key.
- Provides fast access by enabling partitions.
