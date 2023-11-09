SUMMARY OF THE KEY POINTS
Description
The DE module involves setting up data infrastructure, including:
⦁	A production database to store clean, up-to-date data.
⦁	Workflows for fetching, processing, and storing data in the database.
⦁	A feature store for model training.
Implementation Requirements
Workflow Orchestrator
⦁	Create a Dockerfile with a workflow orchestrator (suggested: Apache Airflow) with a graphical interface.
⦁	It should allow scheduling and monitoring of data processing workflows.
⦁	The Docker container should be created from the Dockerfile and run Airflow on port 8882.
⦁	Database:
⦁	Implement a database service (suggested: PostgreSQL) within the docker-compose.yml file.
⦁	The database should be accessible on port 5432 through SQL.
⦁	Database details:
i.	Name: companydata
ii.	Schema: public
iii.	Users: admin with password admin, d_user with password d_user, ml_user with password ml_user.
iv.	Permissions: d_user should have a user role with read-only permissions on the public schema, and ml_user should have the ml_user_role role with all permissions on the public schema.
Data Processing Workflows
⦁	Three workflows must be implemented for processing data found in the s3 bucket daredata-technical-challenge-data. They include customer activity, customer profiles, sales CSVs, and store CSVs.
The workflows are:
1.	Customer Data Load: Load raw data and write to the database as-is.
2.	Sales Data Load and Aggregation: Load and aggregate sales data monthly.
3.	Feature Store: Create a feature store showing customer profiles, customer activity, and the calculated feature_store table with specific columns.
Additional requirements include giving read-access to both the DS and MLE users to all tables.