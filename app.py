import os
from flask import Flask, render_template, request, send_from_directory

import joblib
import pickle
import pandas as pd
from sklearn.decomposition import PCA
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(
    __name__
    )
#env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
#app.config.from_object(env_config)
#secret_key = app.config.get('SECRET_KEY')


@app.get('/')
def home_get():
    #app.logger.info("call came to home_get request data")
    #app.logger.info(request.form)
    #app.logger.info(request.args)
    #app.logger.info(request.headers)
    #app.logger.info("call came to home_ get")
    return render_template('index.html')




@app.post('/')
def home_post():
    #app.logger.info("call came to home_post request data")
    #app.logger.info(request.form)
    #app.logger.info(request.args)
    #app.logger.info(request.headers)
    deck, num, side = request.form['Cabin'].split('/')
    
    testData = {
        "HomePlanet": request.form['HomePlanet'],
        "CryoSleep": request.form['CryoSleep'],
        "Destination": request.form['Destination'],
        "Age": request.form['Age'],
        "VIP": request.form['VIP'],
        "deck": deck,
        "num": num,
        "side": side,
        "RoomService": request.form['RoomService'],
        "FoodCourt": request.form['FoodCourt'],
        "ShoppingMall": request.form['ShoppingMall'],
        "Spa": request.form['Spa'],
        "VRDeck": request.form['VRDeck'],
    }
    prediction, score = run_model(testData)
    error = ""
    transported = "True" if prediction[0] > 0 else "False"
    confidence = score[0][1] * 100
    responseJson = {
        "data" : {
            "transported": transported,
            "confidence": confidence,
        },
        "error": error
    }
    app.logger.info("result from model")
    app.logger.info(responseJson)
    #return responseJson
    return render_template('index.html', data = responseJson)

def getDataFrame(testData):
    """  int, float, bool or category. """

    dataFormat = {
        'HomePlanet': 'category',
        'CryoSleep'   : 'bool',
        'Destination': 'category',
        'Age'   : 'int64',
        'VIP'   : 'bool',
        'deck'   : 'category',
        'num'   : 'int',
        'side'   : 'category',
        'RoomService'   : 'float',
        'FoodCourt'   : 'float',
        'ShoppingMall'   : 'float',
        'Spa'   : 'float',
        'VRDeck'   : 'float',
        }

    #app.logger.info("call came to getDataFrame")
    dataFrame = pd.DataFrame(pd.json_normalize(testData)).astype(dataFormat)
    #app.logger.info(" DataFrame before running LabelEncoder")
    #app.logger.info(dataFrame.head())
    dataFrame = runLabelEncoder(dataFrame)
    #app.logger.info(" getDataFrame types after running LabelEncoder")
    #app.logger.info(dataFrame.dtypes)
    #app.logger.info(" DataFrame after running LabelEncoder")
    #app.logger.info(dataFrame.head())
    return dataFrame



def runLabelEncoder(dataFrame):
    """
    https://stackoverflow.com/a/71463479/3148856
    https://stackoverflow.com/a/28658869/3148856
    """
    label_columns = ["HomePlanet", "CryoSleep","deck","side", "Destination" ,"VIP"]
    encoderDict = joblib.load('LabelEncoderClasses.joblib')
    #app.logger.info("printing LabelEncoderClasses")
    #app.logger.info(encoderDict)
    for col in label_columns:
        encoder = LabelEncoder()
        encoder.classes_ = encoderDict[col]
        dataFrame[col] = dataFrame[col].astype(str)
        dataFrame[col] = encoder.transform(dataFrame[col])
    return dataFrame


def runPCA(testData):
    app.logger.info("call came to runPCA")
    selected_columns_for_pca = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa']
    data = testData[selected_columns_for_pca]
    app.logger.info("printing data in runPCA before fit_transform")
    app.logger.info(data)
    n_components = 2  #number of new columns pca
    pca = PCA(n_components = n_components, svd_solver = 'auto')
    principal_components = pca.fit_transform(data)
    pc_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    testData["pca_feature_1"]=pc_df['PC1']
    testData["pca_feature_2"]=pc_df['PC2']
    testData.drop(['RoomService','FoodCourt','ShoppingMall','Spa'],axis=1,inplace=True)
    return testData

def run_model(testData):
    """
    https://stackoverflow.com/a/56440689/3148856
    """
    #app.logger.info("call came to run_model")
    dataFrame = getDataFrame(testData)
    #app.logger.info("printing dataframe returned from getDataFrame")
    #app.logger.info(dataFrame.head())
    #dataFrame = runPCA(dataFrame)
    #app.logger.info("printing dataframe returned from runPCA")
    #app.logger.info(dataFrame.head())
    dataFrame = dataFrame.reindex(columns=['HomePlanet', 'CryoSleep', 'Destination', 'Age', 'VIP', 'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', 'VRDeck', 'deck', 'num', 'side'])

    pickel_file_name = 'model.pickle'
    with open(pickel_file_name, 'rb') as pickle_file:
        pickel_model = pickle.load(pickle_file)
        setattr(pickel_model, 'verbosity', 3)
        #app.logger.info("printing model info")
        #app.logger.info(type(pickel_model))
        prediction = pickel_model.predict(dataFrame)
        app.logger.info("prediction")
        app.logger.info(prediction)
        score = pickel_model.predict_proba(dataFrame)
        app.logger.info("confidence score")
        app.logger.info(score)
        return (prediction, score)

    # XGBmodel = XGBClassifier({'nthread': 2})
    # XGBmodel.load_model('XGBModel.model') 
    # app.logger.info("printing model")
    # app.logger.info(XGBmodel)
    # prediction = XGBmodel.predict(dataFrame)
    # app.logger.info("printing prediction")
    # app.logger.info(prediction)
    # return prediction
    
    



# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/about')
def about():
    return render_template('index.html')

