targetScope = 'subscription'

param rgpName string
param rgpLocation string

resource rgp 'Microsoft.Resources/resourceGroups@2024-03-01' = {
  name: rgpName
  location: rgpLocation
}

output rgpId string = rgp.id
output rgpName string = rgp.name
output rgpLocation string = rgp.location
