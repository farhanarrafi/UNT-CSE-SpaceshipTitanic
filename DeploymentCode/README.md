# Spaceship Titanic Project for CSCE 5214 Software Development for AI Class


## Project Proposal Link:

https://docs.google.com/document/d/1OQJ_ny5uwrzpezHdD44vjsxkhOW2UOv6csOp5z1E2OM/edit#heading=h.dxcszpkfj0qm

## Jira Link for project:

https://untworkspace.atlassian.net/jira/software/projects/SST/boards/1

Here we can find all tasks that "need to be done", and are "currently in progress" and tasks "that are done".


## Project notebook link:

https://colab.research.google.com/drive/1l3euQVySNzK60mRTqWrTAGPcUR8ePPlx

## Project Run Instructions:
1. After downloading code, open a terminal in root folder and run the following code to setup virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
2. Now install required modules:
```
pip install -r requirements.txt
```
3. To run the code, run the following code:
```
FLASK_ENV=development flask run --debug
```

To update requirements file after lib install, run:
```
python3 -m pip freeze > requirements.txt
```

## ML Dummy Model Source:

https://www.kaggle.com/code/farhanarrafi/spaceship-titanic-minimum-code-0-7725/edit


## References:
1. https://realpython.com/flask-by-example-part-1-project-setup/
2. https://realpython.com/flask-by-example-integrating-flask-and-angularjs/
3. https://github.com/shea256/angular-flask
4. [How to save and load your Scikit-learn models in a minute - AnalyticsVidya](https://medium.com/analytics-vidhya/save-and-load-your-scikit-learn-models-in-a-minute-21c91a961e9b)
