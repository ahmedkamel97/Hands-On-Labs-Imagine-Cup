# Welcome to Hands-On Labs

## This document contains information about all the components within our software submission, all of the submission can be also found in our GitHub repository.

### GitHub repository can be found at: https://github.com/ahmedkamel97/Hands-On-Labs-Imagine-Cup

# Primary Components of our project are available within the folders in the submission and will be briefly introduced below:

## Web Application:

* For our web application we currently have two versions; one that is live at: https://robotarm.net
This version is not the latest, but it is more stable so we use it for testing the lab with students.

* The second version is used for development and is connected to this  GitHub repository, you can view it from here: http://hands-on-labs.azurewebsites.net/

## * Please note that we currently do not have the capacity to keep the hardware and streaming live 24/7, if you wish to experiment with the robot in real-time, please let
##us know at a.kamel@minerva.kgi.edu and we can schedule time to have the live streaming active.

* If you wish to run our web application on your local machine, please follow these instructions:
### Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
Creation of virtualenv:

    $ virtualenv -p python3 venv

If the above code does not work, you could also do

    $ python3 -m venv venv

To activate the virtualenv:

    $ source venv/bin/activate

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate

Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt


##### Run Application

Start the server by running:

    $ export FLASK_ENV=development
    $ export FLASK_APP=web
    $ python3 -m flask run


## Arduino Code:

* This folder contains the firmware running on the Arduino connected to the robotic arm, this code is CRITICAL as it contains our robot model and all the instructions related with out hardware.   

## Raspberry Pi Python Scripts:

* This Python Script is how our robot communicates with our web application, this script is constantly running on a Raspberry Pi that is connected with the Arduino, the primary purpose of this script is pulling the information from the website and fetching it to the robotic arm.

## Forward Kinematics:

* This folder contains a Python Notebook .ipynp that contains instructions and python code that calculates the forward and inverse Kinematics of the robot. This notebook was used in our testing classes with students.

## UI:

* The current UI on our web app is just for testing, however, we developed a much better and user friendly UI that we are working on deploying.

* This folder contains a PDF with our new UI. However, you can view our prototype UI/UX from here: https://xd.adobe.com/view/fb8a1738-8f9b-4e8c-83d1-eed0ef03d859-aed9/?fullscreen

## Guides:

* This folder contains two guides about how the electromechanical components of the robotic arm were assembled.

## Images:

* This folder contains some images for the project.
