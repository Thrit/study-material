param vaultsName string
param location string = resourceGroup().location

var vaultURL = environment().gallery
/* 'https://${vaultsName}.vault.azure.net/' */

resource vaultsNameResource 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-${vaultsName}'
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    accessPolicies: []
    enabledForDeployment: false
    enabledForDiskEncryption: false
    enabledForTemplateDeployment: false
    enableSoftDelete: true
    softDeleteRetentionInDays: 90
    enableRbacAuthorization: true
    vaultUri: vaultURL
    provisioningState: 'Succeeded'
    publicNetworkAccess: 'Enabled'
  }
}

output vaultsNameResourceId string = vaultsNameResource.id
