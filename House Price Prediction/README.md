# California Housing Predictions using Linear Regression

**Required Software and Tools**
1. github account www.github.com
2. heroku account www.heroku.com
3. pycharm IDE community version

California Housing dataset
--------------------------

**Data Set Characteristics:**

    :Number of Instances: 20640

    :Number of Attributes: 8 numeric, predictive attributes and the target

    :Attribute Information:
        - MedInc        median income in block group
        - HouseAge      median house age in block group
        - AveRooms      average number of rooms per household
        - AveBedrms     average number of bedrooms per household
        - Population    block group population
        - AveOccup      average number of household members
        - Latitude      block group latitude
        - Longitude     block group longitude

* Our attributes will be MedInc and HouseAge for the prediction of prices in 
the multiple of Thousand Dollars. 

## Deployment on Heroku
**Requirements** <br>
* Install Heroku CLI and login from cli
* Create Procfile:Heroku file to specify commands need to deploy app on heroku.<br>
* Update requirements: requirements.txt

**Direct From Heroku** <br>
* Go to Heroku interface and deploy direct by choosing git repo in the options

## Deployment on Docker 
* FROM python:3.7        % version of python
* LABEL authors="ManishForceBolt"  % name of the author
* ENTRYPOINT ["top", "-b"] % Optional
# Creating Docker file as app. Copying all from . / current file to file name app 
* COPY . /app


# Making app as Working Directory 
* WORKDIR /app
* RUN pip install -r requirements.txt
* EXPOSE $PORT

# Binding  
* Port exposed is Binding with the local IP-address 0.0.0.0 
* CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

# Create to working directory Local
* .github and workflows directory 
* main.yaml file to workflows directory 
  *     :These will save the complete workflow
