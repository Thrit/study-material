targetScope = 'subscription'

param resourceGroupName string = 'rgp-test'
param location string = 'northeurope'

param storageAccountName string = 'saccnedev'
param blobStorageName string = 'landing-zone'

param webAppName string = 'web-app-test-xd'
param appServiceName string = 'asp-test'
param skuName string = 'F1'
param skuTier string = 'Free'

param vaultsName string = 'us-vault'


module resourceGroupModule './resource-group-template.bicep' = {
  name: '${resourceGroupName}-resourceGroupResource-create'
  scope: subscription()
  params: {
    rgpName: resourceGroupName
    rgpLocation: location
  }
}

module storageAccountModule './storage-account-template.bicep' = {
  name: '${storageAccountName}-storageAccountResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    storageAccountName: storageAccountName
    location: location
  }
}

module blobStorageModule './blob-storage-template.bicep' = {
  name: '${blobStorageName}-blobResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [storageAccountModule]
  params: {
    storageAccountNameResource: storageAccountName
    blobStorageName: blobStorageName
  }
}

module storageAccountModule './blob-storage-template.bicep' = {
  name: '${resourceGroupName}-storageAccountResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    storageAccountName: storageAccountName
    location: location
    blobStorageName: blobStorageName
  }
}
module webAppModule './web-app-template.bicep' = {
  name: '${resourceGroupName}-webAppResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    webAppName: webAppName
    location: location
    appServicePlanName: appServiceName
    skuName: skuName
    skuTier: skuTier
  }
}

module keyVaultModule './key-vault-template.bicep' = {
  name: '${resourceGroupName}-keyVaultResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    vaultsName: vaultsName
    location: location
  }
}

// az deployment sub create -l northeurope --template-file ./iac-resources/main.bicep
