# Data Migration and Automation using Azure

This is an end to end project done using Azure. The main objective is to migrate on premise data to cloud using Azure implementing automated pipelines employing CI/CD actions. 

The techniques implemented in the project are listed below:

- Environment setup
- Data Ingestion
- Data Transformation
- Data Loading
- Data Reporting
- Build End to End Pipeline Testing

The tools employed in the project are listed below:

- Azure Data Factory
- Azure Data Lake
- Azure Databricks
- Azure Synapse Analytics
- Azure Active Directory
- Azure Key Vault
- Microsoft PowerBI
- Microsoft SQL Sever Studio

The database used in the project is AdventureWorkLT2017 which consists of ten tables of two schema "dbo" and "SalesLT". Initially, the data is loaded in Microsoft SQL server studio.

# Environment Setup

The resource group consisting of all required files is created in Azure portal. A login sql script is written in order to connect the on premise database to Azure. The reader access is provided to the user in the studio.

# Data Ingestion

Azure Data Factory (ADF) is mainly used for data ingestion and load it into Data Lake which is a storage solution. The connection between the ADF and on prem database is established using a self hosted integration runtime and Azure Key Vault in which secrets can be created. AKV is useful in secure login purpose. The data is extracted from the database using the pipelines in which various activities like lookup, foreach and copy_table. All the activities must be connected. After extracting the data, the data is loaded into Data Lake (ADL). The connection between ADF and ADL using Auto Resolve integration runtime. The ADL consists of various layers like bronze, silver and gold. The bronze layer consists of true data, the data must be transformed and the loaded into silver and gold layers.

# Data Transformation

Azure Databricks (ADB) helps in data transformation. Here the notebooks can be created in the workspace. Compute cluster is created and the script can be wriiten in python, pyspark or sql. The connection between ADL and ADB is established using credential pass through method. The main tranformations like data time to date format transformation, column name transformation, aggregation etc can be done in the ADB using data trandformation scripts. Finally, the data is loaded into gold layer of ADL in delta format. These activities are attached to the pipeline in ADF.

# Data Loading

Azure Synapse Analytics (ASA) is used in order to create the database similar to original on premise SQL database. Pipelines are created over here to get the metadata and load the load using activities getmetadata, foreach. All the activities are connected to create the pipeline. Finally all the changes are published.

# Data Reporting

An interactive dashboard is created using PowerBI. The data is loaded, various visualizations are used to create the dashboard. DAX expressions like SUM, COUNT, CALCULATE, FILTER etc are also used for effective visualizations.

# Building of End to End Pipeline Testing

Azure Active Directory (AAD) is helpful in creating security groups and security principles foe ensuring security. It is helpful in Identity and Access Management (IAM) and producing access tokens to ensure secure operations. Finally, all the pipelines are automated on daily basis to ensure integrated continuous integration and continuous delivery or deployment of the data.
