param storageAccountNameResource string
param blobStorageName string

resource storageAccountParent 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {
  name: storageAccountNameResource
}

resource storageAccountNameBlob 'Microsoft.Storage/storageAccounts/blobServices@2023-01-01' = {
  parent: storageAccountParent
  name: 'default'
  properties: {
    cors: {
      corsRules: []
    }
    deleteRetentionPolicy: {
      allowPermanentDelete: false
      enabled: true
      days: 7
    }
    containerDeleteRetentionPolicy: {
      enabled: true
      days: 7
    }
  }
}

resource storageAccountNameBlobContainer'Microsoft.Storage/storageAccounts/blobServices/containers@2023-01-01' = {
  parent: storageAccountNameBlob
  name: 'blob-${blobStorageName}'
  properties: {
    immutableStorageWithVersioning: {
      enabled: false
    }
    defaultEncryptionScope: '$account-encryption-key'
    denyEncryptionScopeOverride: false
    publicAccess: 'None'
  }
}

output storageAccountNameBlobContainerId string = storageAccountNameBlobContainer.id
