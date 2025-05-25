# M3 Lab 3

In this lab, you'll build a RAG chatbot app to answer questions about unstructured data (*i.e.* content from DOCX files). 

Briefly, the RAG pipeline that you'll use is handled by [Cortex Search](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-search/cortex-search-overview).

Here are 2 parameters that you'll tweak:
- *chunk size*
- *chunk overlap*

which are set to 1800 and 250, respectively.

## Creating this Streamlit App in Snowflake
1. Log in to Snowflake Snowsight
2. In the left sidebar, click on "Projects" > "Streamlit" to bring up the Streamlit workspace
3. In the top-right corner, click on "+ Streamlit App" to create a Streamlit app
4. Give your app a title
5. Choose the avalanche database and schema that you created in module 2
6. Keep all other settings at default and click on “Create”
7. An example Streamlit app should appear- delete all the existing code from the example app
8. Copy the code from the streamlit_app.py file on our repo:
https://github.com/https-deeplearning-ai/rapid-prototyping-with-streamlit/blob/master/M3/Lab3/streamlit_app.py
9. Paste the streamlit_app.py code into the left code of the Snowflake Streamlit editor panel
10. Click on Run to spin up the app

Follow along with the video for the rest. 



