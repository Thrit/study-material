# Describe the Core Architectural Components of Azure

## [Unit 1: Learning Objectives](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/1-introduction)
After completing this module, you’ll be able to:
- Describe Azure regions, region pairs, and sovereign regions.
- Describe Availability Zones.
- Describe Azure datacenters.
- Describe Azure resources and Resource Groups.
- Describe subscriptions.
- Describe management groups.
- Describe the hierarchy of resource groups, subscriptions, and management groups.

## [Unit 5: Describe Azure Physical Infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/5-describe-azure-physical-infrastructure)
### Physical Infrastructure
- Azure's physical infrastructure resembles a large corporate datacenter.

### Regions
- A region is a geographical area on the planet that contains at least one, but potentially multiple datacenters that are nearby and networked together with a low-latency network.

### Availability Zones
- Availability zones are physically separate datacenters within an Azure region.
- They are set up to be isolation boundaries, ensuring continued operation if one zone goes down.
- Azure services supporting availability zones are categorized as Zonal services, Zone-redundant services, and Non-regional services.

### Region Pairs
- Most Azure regions are paired with another region within the same geography to reduce the chances of interruptions during catastrophes or events.

### Sovereign Regions
- Sovereign regions are instances isolated from the main instance of Azure, often used for compliance or legal purposes.

## [Unit 6: Describe Azure Management Infrastructure](https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/6-describe-azure-management-infrastructure)
### Azure Subscriptions
- Subscriptions are a unit of management, billing, and scale in Azure.
- They serve as both a billing and access control boundary, allowing separate management and cost organization.
- Different subscription types support various organizational structures and access management policies.

### Creating Additional Azure Subscriptions
- Similar to using resource groups, additional Azure subscriptions help separate resources based on function, access, environments, organizational structures, or billing.
