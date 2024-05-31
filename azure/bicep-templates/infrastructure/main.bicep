targetScope = 'resourceGroup'

param resourceGroupName string = 'rgp-dev'
param location string = 'eastus'

// Include the blob storage template as a module
module storageAccountModule './blob-storage-template.bicep' = {
  name: 'storageAccountResource'
  scope: resourceGroup(resourceGroupName)
  params: {
    storageAccountsName: 'usdev'
    location: location
    blobStorageName: 'landing-zone'
  }
}

// Include the key vault template as a module
module keyVaultModule './key-vault-template.bicep' = {
  name: 'keyVaultResource'
  scope: resourceGroup(resourceGroupName)
  params: {
    vaultsName:'us-vault'
    location: location
  }
}

// az deployment group create --resource-group 'rgp-dev' --template-file ./azure_workflow/infrastructure/main.bicep --mode Complete
