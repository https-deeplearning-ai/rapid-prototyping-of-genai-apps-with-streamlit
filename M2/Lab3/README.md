# M2 Lab 3 Deploying to Streamlit Community Cloud

In Module 2 Lab 3, you'll deploy the Streamlit app you have previously built and deployed on the Snowflake platform onto the [Streamlit Community Cloud](https://streamlit.io/cloud).

**Before attempting to deploy your app to the cloud, make sure you have completed the steps in Module 2 Lab 1 and Module 2 Lab 2.**

## Create your own GitHub repository for this Lab
1. You need to upload this lab’s files into a Github repository you will create as follows.
2. Log into your GitHub account
3. On the top-right corner click on the (+) button and select "New repository"
4. Go to the "Repository name*" and type the repository name. For simplicity, let's use `avalanche`
5. Scroll down and check the radio button for the option "Public"
6. Leave the other options by their default setting
7. Click on "Create repository"

## Upload the App files
1. Download the course’s GitHub repository as a ZIP file. Unzip the file and go to folder M2/Lab3. This folder contains the Streamlit app files
2. Now go to the GitHub repository folder created for this Lab. For example, if the GitHub user "learner01" created the repository named "avalanche", the repository should be:
```
  		learner01/avalanche
```
3. In the repository, upload the app files. If the repository is new, click on "uploading an existing file". If the repository already contains some files, above the list of files, select the "Add file" dropdown menu and click "Upload files".
4. Drag and drop the app files from the folder ```M2/Lab3``` into the GitHub repository. You need to drag and drop the following files and folders:
   
    a. File ```README.md```

    b. File ```requirements.txt```

    c. File ```streamlit_app.py```

    d. Folder ```.streamlit/```

    e. Folder ```data/```


5. Once you have dragged and dropped all the files into the repository, click on the green button "Commit changes"

You are set to move on.

## Deploying the app
To deploy your apps to the cloud, you’ll need to sign up for a Streamlit Community Cloud account using your Github login, so that we can link the two accounts for easy deployment. Please log into your GitHub account before you follow these steps.

1. Navigate to Streamlit Community Cloud
2. Click on “Join Community Cloud”
3. Another browser window will pop-up. From here, click on “Continue to Sign-in”
4. Click on “Continue with Github”
5. Click on “Authorize Streamlit”
6. An email will be sent to the email address used on your GitHub account called “Verify your email address” sent from Streamlit Community Cloud
7. Open that email and copy the verification code
8. Go back to the Streamlit Community Cloud sign in and enter the verification code to verify your account

You’re now able to use your Streamlit Community Cloud account and deploy directly from your Github repository

## Deploying to the Community Cloud
To deploy the app you’ve just built:

1. From the home page of Streamlit Community Cloud, click on the “Create App” button on the top-right of your screen
2. Select the option on the left to “Deploy a public app from Github” by clicking on “Deploy Now”
3. In the "Repository" field, enter the Github URL for the repo you want to deploy. In your case, you will use the name you assigned to the repo for this lab.

    For example, the GitHub user `learner01` who created the `avalanche` repo, must type `learner01/avalanche` in the "Repository" field.

4. In the Main File Path field, click on the drop-down menu to drill down to the file for the streamlit_app.py file that you want to deploy
5. Click on "Deploy" and give it a few moments to spin up your new app
6. Once deployed, you will be provided with a link where you can view and share your new app.
