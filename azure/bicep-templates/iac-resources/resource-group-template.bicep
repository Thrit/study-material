targetScope = 'subscription'

param rgpName string
param rgpLocation string

// Create the resource group
resource rgp 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: rgpName
  location: rgpLocation
}

// Output the resource group details
output rgpId string = rgp.id
output rgpName string = rgp.name
output rgpLocation string = rgp.location
