Workflow Orchestrator (Airflow)
1. Dockerfile for Airflow
I writed a Dockerfile that sets up Apache Airflow.
This include Airflow itself, the dependencies, and the configurations for its UI to be exposed on port 8082.
2. Airflow Scheduling and Backfilling:
I Defined Directed Acyclic Graphs (DAGs) for each workflow.
Also i configured DAGs to schedule tasks and enable automatic backfilling.
3. docker-compose Integration:
Added Airflow as a service in docker-compose.yml.
and Mapped the Airflow UI port to 8082.
Database (Postgres)
1. Docker-compose Service:
Defined a Postgres service in my docker-compose.yml.
Exposed the database on port 5432.
and, the service named 'operational-db'.
2. Database Configuration:
I initialize the companydata database with the public schema.
also, create users admin, ds_user, and mle_user with the specified roles and permissions.
3. Permissions and Roles:
Hear, i set up the roles as required, granting the appropriate permissions to each user.
Data Processing Workflows
1. Customer Data Load
Created an Airflow DAG that triggers a one-off task.
This fetches customer data files and writes them to the Postgres database without altering the data.
2. Sales Data Load and Aggregation
Developed a DAG for monthly processing of sales data.
I also create the sales and monthly_sales tables.
finally, aggregate data and insert it into the monthly_sales table.
3. Feature Store
I have to implement a DAG that creates a feature_store table.
The DAG must process and join data from multiple sources into this table.
Access Permissions
I give the ds_user has read-only access to all tables.
and, make sure the mle_user has all permissions on the public schema.
