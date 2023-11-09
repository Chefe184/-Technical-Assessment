-- Connect to the PostgreSQL container and open the psql shell
CREATE ROLE ds_user WITH LOGIN PASSWORD 'ds_user';
CREATE ROLE mle_user WITH LOGIN PASSWORD 'mle_user';
GRANT ds_user_role TO ds_user;
GRANT mle_user_role TO mle_user;
-- For admin, you could manage this within the environment variables or do it within the database.

-- Create roles with the specified permissions
CREATE ROLE ds_user_role;
CREATE ROLE mle_user_role;

-- Grant permissions
GRANT USAGE ON SCHEMA public TO ds_user_role;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO ds_user_role;

GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO mle_user_role;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO mle_user_role;
GRANT ALL PRIVILEGES ON SCHEMA public TO mle_user_role;

-- Adjust this according to your actual database setup and security practices

