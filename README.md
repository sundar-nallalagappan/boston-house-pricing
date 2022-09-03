### Boston-house-pricing


### Software & Tools requirements

1. [GithubAccount](https://github.com)
2. [HerokuAccount](https://heroku.com)
3. [GITCLI](https://git-scm.com/downloads)
4. [VSCodeIDE](https://code.visualstudio.com)


### Steps

1. Git repository has been created for this end to end Boston price prediction project

https://github.com/sundar-nallalagappan/boston-house-pricing.git

I have cloned this Git repo to my local machine using the below command

git clone https://github.com/sundar-nallalagappan/boston-house-pricing.git


2. Create a new environment specifc to our project

Below command is to create environment in the current working directory (we have used this)

create -p  boston_env1 python==3.7

(or)

Below command is common command to create an env

conda create --name boston_env python==3.7


3. Activate the environment

conda activate boston_env1/   (To activate the env created in the path)

or

conda activate boston_env


4. Other useful conda commands to recheck the environment

conda info --envs

conda env list

Note: I was able to activate the environment from command prompt terminal only


5. Configure GIT to integrate the code 

    a. git config --global user.name "Sundar Nallalagappan"

    b. git config --global user.email "nsundar.1990@gmail.com"

    c. Add the files to be committed to git repository
        
        git add requirements.txt        ==> This will move the file to stagged changes

        git add .                       ==> To add all the files
        
        git status                      ==> To check the state of each file in local repo

        git commit -m "Initial commit: Includes requirement.txt & readme file"

        git push origin main

6. Create app.py file with Flask to create micro web-service - To expose the model as an API
    
    * Points to remember:
    
        * render template destination files (Ex: home.html) to reside in templates folder
        * Standard scaler to be applied prior to inferencing
        * Make sure to reshare the raw data (from (13,1) to (1,13))
        * Jsonify the output and return the value to the client

7. Run the app.py from the terminal - Model will be exposed as an API in local client
   http://127.0.0.1:5000/predict_api

8. Prepare a test data in Json format and test the same via Postman in POST method
'''
{
    "data" : {
        "CRIM":0.00632,
        "ZN":18.0,
        "INDUS":2.31,
        "CHAS":0.0,
        "NOX":0.538,
        "RM":6.575,
        "AGE":65.2,
        "DIS":4.0900,
        "RAD":1.0,
        "TAX":296.0,
        "PTRATIO":15.3,
        "B":396.90,
        "LSTAT":4.98
    }
}
'''

9. Created predict method to consume the value from html form and then to make inference out of it. 

# Deploy the app to HEROKU cloud platform

1. Proc file to be created. Contains the commands to be executed as soon as the app gets started

2. Commands are based out of Green unicorn (Python http server for WSGI app enables concurrency)

3. Below are commands in proc file

    web: gunicorn app:app       ==> gunicorn takes care of concurrency when multiple requests hits the app; app specifies app.py and second instance of app indicates the app object created out of Flask within app.py

    




