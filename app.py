import os
from flask import Flask, render_template, request, send_from_directory

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

'''
Passenger {
  HomePlanet: 'Earth' | 'Europa' | 'Mars';
  CryoSleep: boolean;
  Destination: 'TRAPPIST-1e' | '55 Cancri e' | 'PSO J318.5-22';
  Age: number;
  VIP: boolean;
  RoomService: number;
  FoodCourt: number;
  ShoppingMall: number;
  Spa: number;
  VRDeck: number;
}
'''


@app.get('/')
def home_get():
    app.logger.info("call came to home_ get")
    return render_template('index.html')




@app.post('/')
def home_post():
    app.logger.info("call came to home_post request data")
    app.logger.info(request)
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
    resultFromModel = run_model(testData)
    app.logger.info("result from model")
    app.logger.info(resultFromModel)
    return render_template('index.html', response = {})

def getDataFrame(testData):
    """  int, float, bool or category. """

    label_cols = ["HomePlanet", "CryoSleep","deck","side", "Destination" ,"VIP"]

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

    app.logger.info("call came to getDataFrame")
    dataFrame = pd.DataFrame(pd.json_normalize(testData)).astype(dataFormat)
    dataFrame = runLabelEncoder(dataFrame, label_cols)
    app.logger.info(" getDataFrame types")
    app.logger.info(dataFrame.dtypes)
    return dataFrame



def runLabelEncoder(dataFrame,columns):
    for col in columns:
        dataFrame[col] = dataFrame[col].astype(str)
        dataFrame[col] =  LabelEncoder().fit_transform(dataFrame[col])
    return dataFrame


def runPCA(testData):
    app.logger.info("call came to runPCA")
    selected_columns_for_pca = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa']
    data = testData[selected_columns_for_pca]
    app.logger.info("printing data in runPCA before fit_transform")
    app.logger.info(data)
    n_components = 2  #number of new columns pca
    pca = PCA(n_components = n_components)
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
    app.logger.info("call came to run_model")
    dataFrame = getDataFrame(testData)
    app.logger.info("printing dataframe returned from getDataFrame")
    app.logger.info(dataFrame.head())
    dataFrameWithPCA = runPCA(dataFrame)
    app.logger.info("printing dataframe returned from runPCA")
    app.logger.info(dataFrame.head())
    pickel_file_name = 'model.pickle'
    with open(pickel_file_name, 'rb') as pickle_file:
        pickel_model = pickle.load(pickle_file)
        app.logger.info("printing model info")
        app.logger.info(type(pickel_model))
        dataFrameWithPCA = dataFrameWithPCA.reindex(columns=['HomePlanet', 'CryoSleep', 'Destination', 'Age', 'VIP', 'VRDeck', 'deck', 'num', 'side', 'pca_feature_1', 'pca_feature_2'])
        return pickel_model.predict(dataFrameWithPCA)



# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')


@app.route('/about')
def about():
    return render_template('index.html')

