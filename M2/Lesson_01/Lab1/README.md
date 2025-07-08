# Avalanche Lab: Analyzing Shipping Logs with Snowflake + Python

Welcome to the Avalanche prototype lab! In this exercise, you’ll analyze raw shipping log data to extract useful insights about delivery patterns, delays, and customer experiences.

This lab is designed as part of the **Rapid Prototyping with GenAI + Streamlit on Snowflake** course. You’ll use Snowflake’s Notebook environment along with Python to:

- Ingest and parse raw markdown data
- Clean and structure the shipping records
- Extract relevant fields like delivery status, dates, product names, and customer satisfaction
- Load the structured data into a Snowflake table
- Optionally explore the results using GenAI or Streamlit

## 📂 Files

- `lab_shipping_logs.ipynb` — Main Jupyter notebook for the lab
- `shipping-logs.md` — Raw markdown file containing sample shipping log data

## ✅ Prerequisites

- A working Snowflake account with access to Snowsight Notebooks
- Python enabled in your Snowflake environment
- Snowpark Python and `python-dotenv` installed (if running locally)
- Basic familiarity with Python, Pandas, and SQL

## 🚀 Instructions

1. Upload both `lab_shipping_logs.ipynb` and `shipping-logs.md` to your Snowflake Notebook or local Jupyter environment.
2. Open the notebook and follow the steps to:
   - Read in the markdown file
   - Parse the logs using string operations or regex
   - Structure the data into a usable Pandas or Snowflake DataFrame
   - Load the data into a Snowflake table
3. Optionally, you can use Snowflake's Cortex GenAI features or Streamlit to visualize results.

## 🎯 Learning Objectives

By completing this lab, you’ll be able to:
- Handle semi-structured markdown data in Snowflake Notebooks
- Transform real-world messy data into structured formats
- Build Snowflake pipelines that are GenAI-ready

---

Feel free to fork, extend, or integrate this lab into your own GenAI app!
