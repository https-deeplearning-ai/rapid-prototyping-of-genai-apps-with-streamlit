-- STEP 1
-- Create the avalanche database and schema
CREATE DATABASE IF NOT EXISTS avalanche_db;
CREATE SCHEMA IF NOT EXISTS avalanche_schema;

-- STEP 2
-- Option 1: Manual upload to Stage
-- Create the stage for storing our files
-- Uncomment code block below for this option:
--
CREATE STAGE IF NOT EXISTS avalanche_db.avalanche_schema.customer_reviews
  ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE')
  DIRECTORY = (ENABLE = true);


-- STEP 3
-- List the contents of the newly created stage
ls @avalanche_db.avalanche_schema.customer_reviews;


-- STEP 4
-- Read single file
-- Uncomment lines below to use:
--
-- SELECT
--   SNOWFLAKE.CORTEX.PARSE_DOCUMENT(
--     @avalanche_db.avalanche_schema.customer_reviews,
--     'review-001.docx',
--     {'mode': 'layout'}
--   ) AS layout;
