# GT Tech Challenge

#### Section 1
1. The source data is read from the folder *sourceData/* every hour. After processing is done, the source files will be put into the folder *sourceData/completed/*. 
2. The successful applications are generated in the folder at *processedData/successful/*; for failed cases, they are generated in the folder at *processedData/unsuccessful/*.
3. The pipeline is scheduled by Airflow on hourly basis. In the file airflow.cfg, please specify the parameter dags_folder to point at the project folder for the airflow to locate the dags to run.

#### Section 2
1. The image entity\_diagram.png describes the schema of the database. It follows the star schema, in which the order\_table is the fact table and the other tables are different dimensions.
2. For initializing the PostgreSQL database, please use the command *bash run.sh* to build and run the docker, in which the *init.sql* will be automatically executed and create the tables ready in the database. The following commands can be used to check and operate the docker containers. 
*docker ps*  -- list all the containers
*docker stop <container_name>*  -- stop container
*docker rm <container_name>*  -- remove container
3. The file *analysis.sql* can be used for the analysts to do analysis on the two questions:
*Which are the top 10 members by spending*
*Which are the top 3 items that are frequently brought by members*
#### Section 3
The 2 images *design1.png* and *design2.png* are for each scenario, respectively.
1. The Design I is on top of Google Cloud Platform. The application is scheduled by Airflow and wrapped up as API service for users to call. The Logistics/Analytics/Sales teams use their corresponding credentials to get the JWT token and then operate on the database per their allowed access. BigQuery is the datawarehouse.
2. The Design II is based on AWS and the key points are added below the diagram.
#### Section 4
The graph of covid-19 cases in Singapore is displayed in 2 ways, python pyplot and Tableau. The python scripts and dataset can be found in the folder.
#### Section 5
Three models are used for modeling and prediction, which are SVM, Decision Tree, and XGboost. The parameter tuning is significant in modeling, so that the grid search is used to decide the optimized parameter combination. 
The general workflow is to load the data --> label encoding the features --> segregate the features and the target --> split the training and testing datasets --> train the model --> evaluate the model --> predict for the specific scenario.
The 3 models don't achieve satisfied accuracy rate in the practice, possibly due to the features available in the source dataset may not be a good set of features to interpret the buying price.