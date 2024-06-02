targetScope = 'subscription'

param resourceGroupName string = 'rgp-test'
param location string = 'northeurope'
param storageAccountName string = 'saccnedev'
param blobStorageName string = 'landing-zone'
param webAppName string = 'web-app-test-xd'
param appServicePlanName string = 'asp-test'
param skuName string = 'B1'
param skuTier string = 'Basic'
param vaultsName string = 'kv-ne-vault'
param linuxFxVersion string = 'PYTHON|3.11'
param functionAppName string = 'function-app-test-xd'

// az deployment sub create -l northeurope --template-file ./iac-resources/main.bicep

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

module appServicePlanModule './app-service-plan-template.bicep' = {
  name: '${appServicePlanName}-webAppResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    location: location
    appServicePlanName: appServicePlanName
    skuName: skuName
    skuTier: skuTier
  }
}

module webAppModule './web-app-template.bicep' = {
  name: '${webAppName}-webAppResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule, appServicePlanModule]
  params: {
    webAppName: webAppName
    location: location
    appServicePlanName: appServicePlanName
    linuxFxVersion: linuxFxVersion
  }
}

module functionAppModule './azure-function-template.bicep' = {
  name: '${functionAppName}-webAppResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule, appServicePlanModule]
  params: {
    functionAppName: functionAppName
    location: location
    appServicePlanName: appServicePlanName
    linuxFxVersion: linuxFxVersion
  }
}

module keyVaultModule './key-vault-template.bicep' = {
  name: '${vaultsName}-keyVaultResource-create'
  scope: resourceGroup(resourceGroupName)
  dependsOn: [resourceGroupModule]
  params: {
    vaultsName: vaultsName
    location: location
  }
}
