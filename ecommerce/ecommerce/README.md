# Hydroworld online shopping app

## What is the application about?
This application was developed to be hosted on render 
## Information regarding the data.
The data was gotten from Open Source
## Features

Hydroworld web application offers you the following features .
* Store feature under the visualize option helps you to view the data in tabular form.
* Search in the table view page helps you to view specific product. 
* Login helps you to visit the site as a user

## Requirements

All the packages and libraries required for this application to run can be found in requirements.txt file.

## Installation

To install the application, you need to clone/download the application  

```bash
git clone "repo_link"
```
Run the below command to install pyenv

```bash
pyenv update
pyenv install 3.10.7 # to install the pyenv on your server.
```

You need to create a virtual environment. Set present location in termial to root directory of the project and then run the following commands to create and start the virtunal environment.  
```bash
pyenv local 3.10.7 # this sets the local version of python to 3.10.7
python3 -m venv .venv # this creates the virtual environment for you
source .venv/bin/activate # this activates the virtual environment
pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.
```

To install the dependencies run the following command.
```bash
pip install -r requirements.txt
```




## Deployment

To start the application run the following command from root directory.
```bash
 python3 manage.py runserver
```
To terminate the application use ctrl+c or follow the commands shown in terminal.



## Demo

The application is deployed and you can find it using the below link:
https://hydroplus.onrender.com/

## Credits
The data source for this application was taken from https://www.kaggle.com/datasets/