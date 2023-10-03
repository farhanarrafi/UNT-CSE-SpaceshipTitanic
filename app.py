import os
import pickle
from flask import Flask, render_template, request, send_from_directory

import pandas as pd
from sklearn.decomposition import PCA

app = Flask(__name__)
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
    return render_template('index.html')



@app.post('/')
def home_post():
    testData = {
        "HomePlanet": request['HomePlanet'],
        "CryoSleep": request['CryoSleep'],
        "Destination": request['Destination'],
        "Age": request['Age'],
        "VIP": request['VIP'],
        "RoomService": request['RoomService'],
        "FoodCourt": request['FoodCourt'],
        "ShoppingMall": request['ShoppingMall'],
        "Spa": request['Spa'],
        "VRDeck": request['VRDeck'],
    }
    return render_template('index.html', response = {run_model(testData)})

def getDataFrame(testData):

    dataFrame = pd.DataFrame(testData)
    return dataFrame


def runPCA(testData):
    selected_columns_for_pca = ['RoomService', 'FoodCourt', 'ShoppingMall', 'Spa']
    data = testData[selected_columns_for_pca]
    n_components = 2  #number of new columns pca
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(data)
    pc_df = pd.DataFrame(data=principal_components, columns=[f'PC{i+1}' for i in range(n_components)])
    testData["pca_price"]=pc_df['PC1']
    testData["pca_pricee"]=pc_df['PC2']

    return testData

def run_model(testData):
    dataFrame = getDataFrame(testData)
    dataFrameWithPCA = runPCA(dataFrame)
    pickel_file = 'trained_model.pkl'
    with open(pickel_file, 'rb'):
        pickel_model = pickle.load(pickel_file)
        return pickel_model.predict(dataFrameWithPCA)



# special file handlers and error handlers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

@app.route('/about')
def about():
    return render_template('index.html')

