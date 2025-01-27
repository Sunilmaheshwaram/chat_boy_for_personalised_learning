Project: Chatbot for personalised Learning
Steps for implementing the above project is given below
Step-1: Create a virtual Environment
 Command : source .venv/bin/activate
Step-1: Installing Rasa
 Command : Pip install Rasa
Step-2: check rasa version
 command : rasa --version
After installing Rasa you can see some .yml files for a input and response you have to edit the yml files
Step-3: Editing the NLU.yml
Basically intent is give in the NLU.yml file
Step-4: Domani.yml
The domain.yml files operates on the responses of the bot
Step-5: Rules.yml
The Rules.yml file will be having stories and actions in it
Step-6: Integrating Youtube API
First go to the "Google Cloud Console"
Then - Console
     - Click on API and services
     - Click on New API(select YouTube Data API v3)
     - Click on "Credentials"
     - Click on Generate a Key
Step-7: After generating a Key go to the actions.py file in your project
Step-8: Paste the Key in the actions.py file
Step-9: After pasting the key in the actions.py file test you bot in the backend(Pycharm)
Step-10: For testing the bot
 Commands: rasa run actions.py
          rasa train
          rasa shell
Step-11: Now its time for the UI part with the streamlit,Before run the bot in streamlit integrate the github repo to the project
 Commands: - Git init in bsh
           - git remote add origin <your-repo-url>
           - git add .git commit -m "Initial commit for Streamlit app"
           - git branch -M main  # Or 'master' depending on your repo's default branch
             git push -u origin main
           - Provide username of the github account and password your github repo will be integrated
Step-12: Then its time for the running streamlit,after integrating the project with github
 Command: streamlit run app.py
 Your User interface will be displayed after this command
Step-13: After seeing your UI you can change your UI by updating your app.py code in your project

THESE ARE THE STEPS TO IMPLEMENT THE CHATBOT FOR PERSONLISED LEARNING.
            
 

     

 
