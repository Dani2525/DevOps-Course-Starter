terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">= 2.92"
    }
  }
}

provider "azurerm" {
  features {}
}

data "azurerm_resource_group" "main" {
  name = "OpenCohort21_DaniPhilip_ProjectExercise"
}

resource "azurerm_app_service_plan" "main" {
  name                = "terraformed-asp"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  kind                = "Linux"
  reserved            = true
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "main" {
  name                = "dabi-m12"
  location            = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id

  site_config {
    app_command_line = ""
    linux_fx_version = "DOCKER|daniphilip/hello-world:prod"
  }

  app_settings = {
    "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
    "SECRET_KEY"= "secret-key"
    "mongo_client" = "azurerm_cosmosdb_account.main.connection_strings[0]"
    "mongo_client"= "mongodb://dabi-m12:t0qwxU3V7MZ2Y55mhbnRAtefiGrwJTUHaTO6MhO0Kv8KTW3PX6GKvlon3LF1h8u29BCgQRYE41wgACDbSTzsgg==@dabi-m12.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dabi-m12@"
    "client_id"= "461640fd1000642d0462"
    "client_secret"= "a1a2e8f1dc310351d18b4a3a36493c7edc9c0e22"
  }
}

resource "azurerm_resource_group" "example" {
  name     = "OpenCohort21_DaniPhilip_ProjectExercise"
  location = "West Europe"
}

resource "random_integer" "ri" {
  min = 10000
  max = 99999
}

resource "azurerm_cosmosdb_account" "db" {
  name                = "dani-m12"
  location            = azurerm_resource_group.example.location
  resource_group_name = azurerm_resource_group.example.name
  offer_type          = "Standard"
  kind                = "MongoDB"

  enable_automatic_failover = true

  capabilities {
    name = "EnableAggregationPipeline"
  }

  capabilities {
    name = "mongoEnableDocLevelTTL"
  }

  capabilities {
    name = "MongoDBv3.4"
  }

  capabilities {
    name = "EnableMongo"
  }

  capabilities { 
    name = "EnableServerless" 
  } 

  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 300
    max_staleness_prefix    = 100000
  }

  geo_location {
    location          = "eastus"
    failover_priority = 1
  }

  geo_location {
    location          = "westus"
    failover_priority = 0
  }
}

data "azurerm_cosmosdb_account" "example" {
  name                = "dani-m12"
  resource_group_name = "OpenCohort21_DaniPhilip_ProjectExercise"
}

resource "azurerm_cosmosdb_mongo_database" "example" {
  name                = "dani-m12"
  resource_group_name = data.azurerm_cosmosdb_account.example.resource_group_name
  account_name        = data.azurerm_cosmosdb_account.example.name
  throughput          = 400
}