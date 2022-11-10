<div align="center">
  <h1 align="center">Collection</h1>
  <p align="center">
    My own project to learn
    
  </p>
</div>


## About

Using the Collecion application, the user can share with others Movie which he like to watch. User can only update and delete his own data. Not register user can only looks on others models.

## Table of Contents
* [Getting started](#getting-started)
* [Usage](#usage)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Project Status](#project-status)


## GETTING STARTED

1. Checking Python version.
    - To be able to use this script you'll need to have Python installed, you can check whether you have it installed or not by typing in terminal:  
`python3 --version`  
or:  
`python --version` 
    - This script was written using version 3.9.0 and it is advised to use the same version.
    - If you don't have Python installed you can go to [Python.org](https://www.python.org/downloads/) to download it.
    
 2. Creating Virtual Environment 
    - To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:  
    `python3 -m venv your-env`  
    - Once you’ve created a virtual environment, you may activate it.  
    `source your-env/bin/activate`
    
 3. Download
     - You need to clone repository to your local destination  
    `cd path/to/your/workspace`  
    `git clone https://github.com/robert-adamczyk/Collection`
    
 4. Requirements
    - Once your virtual environment is activated and project is cloned you need to install requirements:  
    `pip install -r requirements.txt`
    
 5. Make your secret key in settings.py     
   ```js
   In settings.py set:
       SECRET_KEY = os.getenv('SECRET_KEY')
   
       DEBUG = os.getenv("DEBUG") == "True"
   
   In manage.py folder create .env file.
   
   Add to .env file variables used in settings.py config: 
       SECRET_KEY = example_name
       DEBUG = True
   ```
    
 ## USAGE
 
 To use this application you need to type (if you're in your workspace directory): 
 
 - `python manage.py migrate`
 - `python manage.py createsuperuser`
 - `python manage.py runserver`  
    
 ## Features
   List the ready features here:
   - user registration/login
   - registrator new user
   - connect with Rest Api
   - add Movie and Director models
   - delete and update model only for owner and superuser
   
  
## Technologies Used:
  - asgiref==3.5.2
  - Django==4.1
  - djangorestframework==3.13.1
  - python-dotenv==0.20.0
  - pytz==2022.2.1
  - sqlparse==0.4.2
  - tzdata==2022.2


## Languages and Tools:
<p align="left"> <a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.sqlite.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" alt="sqlite" width="40" height=40"/> </a> </p>
## Project Status
Project is: _done_


## License

MIT License.
