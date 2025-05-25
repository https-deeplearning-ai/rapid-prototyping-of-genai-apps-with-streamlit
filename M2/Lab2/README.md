# M2 Lab 2 Deploying Your Prototype Internally on Snowflake

In Module 2 Lab 2, you're aggregating all that you've built in prior labs into this Streamlit app that you'll deploy to Streamlit in Snowflake (SiS).

**Before starting this lab, make sure you have created the Avalanche database, schema and stage that we built in the previous lab.**
1. Log in to Snowflake Snowsight
2. In the left sidebar, click on "Projects" > "Streamlit" to bring up the Streamlit workspace
3. In the bright blue button on the top-right corner, click on "+ Streamlit App" 
4. A "Create Streamlit App" window pops up. 
    Enter the following:
    - App title
    - App location: choose your avalanche database and schema
    - Leave app warehouse at default “COMPUTE_WH”
5. Click on Create
6. An example Streamlit app should appear
7. Erase the code from the existing example app
8. In this Github repo folder, copy the code from the file called streamlit_app.py
9. Paste this code into the left code editor panel where you just deleted the example code from. 
10. Click on Run

You’ll walk through this code in more detail with the help of the accompanying lab walkthrough video for Module 2 Lab 2. 
