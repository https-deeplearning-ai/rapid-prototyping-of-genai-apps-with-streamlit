# M3 Lab 1 Using Data Augmentation to Build a Simple Chatbot

In Module 3 Lab 1, you'll start this lab with the prototype you built in Module 2, where you have already created and deployed a prototype that performs sentiment analysis and can visualize the results grouped by time period and product


You can think of this method as building an augmented chatbot on structured data; we're applying the string version of the DataFrame as context directly into the prompt.

## Setup

1. Log in to Snowflake Snowsight
2. In the left sidebar, click on "Projects" > "Streamlit" to bring up the Streamlit workspace
3. In the top-right corner, click on "+ Streamlit App" to create a Streamlit app
    - Give your app a title
    - Choose the avalanche database and schema that you created in module 2
    - Keep all other settings at default and click on “Create”
4. An example Streamlit app should appear- delete all the existing code from the example app
5. Copy the code from the streamlit_app.py file on our repo:
https://github.com/https-deeplearning-ai/rapid-prototyping-with-streamlit/blob/master/M1/Lab3/streamlit_app.py
6. Paste the streamlit_app.py code into the left code of the Snowflake Streamlit editor panel
7. Click on Run to spin up the app. 

The lab video will walk you through the code in more detail. 

## Augmenting our Prompt with Data

The rest of this lab will focus on how we can add additional context to our prompt in order to assist our chatbot in returning better results. 

Since you’re building an app around the Avalanche Dataset, one of the easiest things we can do to augment our prompt is to provide the entire dataset as context to our prompts. However, it would be really clunky to copy and paste an entire dataframe, you’ll use code to help create additional context for your prompt. 

In the first part of the lab, you walked through the section of code that reads in our customer reviews as a pandas dataframe. You then converted it to a string and stored the output in a variable named dataframe_context that you can feed to our prompt in a prompt section titled “context”. 

Here's the prompt:
```
[INST]
You are a helpful AI chat assistant. Answer the user's question based on the provided
chat history and the context data from customer reviews provided below.

Use the data in the <context> section to inform your answer about customer reviews or sentiments
if the question relates to it. If the question is general and not answerable from the context
or chat history, answer naturally. Do not explicitly mention "based on the context" unless necessary for clarity.

<chat_history>
{chat_history}
</chat_history>

<context>
{dataframe_context}
</context>

<question>
{user_question}
</question>
[/INST]
Answer:
```
