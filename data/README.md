# 🗻 Avalanche Data Set

Avalanche is a hypothetical company that sells winter sports gear. 

This data set is comprised of:
- Customer reviews
- Product catalog
- Order history
- Shipping log

## What we're building

We're tasked with the goal of figuring out the general sentiment that customers have towards the company's products. Therefore, we'll use the ***customer reviews*** data to build a dashboard app with Streamlit.

## Unstructured data

The unstructured version of the data is provided in the `files/` directory. From there you can find additional sub-directory called `files/customer_reviews` (that contains a collection of `DOCX` files), `files/order_history` (that contains a collection of `PDF` files), etc.

To setup the database and upload to a stage on the Snowflake platform, you can use the SQL code provided in the `setup.sql` file.
