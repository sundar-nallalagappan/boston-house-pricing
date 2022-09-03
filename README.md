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

        git status                      ==> To check the state of each file in local repo

        


