
import tensorflow as tf
import numpy as np 
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd
from sklearn import preprocessing


def prediction(val1, val2, val3, model):
    val1, val2, val3 = float(val1), int(val2), float(val3)
    X = np.array([val1, val2, val3])
    X= X.reshape(1, -1)
    X = StandardScaler().fit_transform(X )
    #X = X.reshape(1, 1, 3)
   
    pred = model.predict(X)
    return round(pred[0][0])


def csv_prediction(file, model):
    data = pd.read_csv(file)
    data = data.drop(['Unnamed: 0'	], axis=1)
    X = encoder(data)
   
    X = StandardScaler().fit_transform(X)
    pred_array = model.predict(X)
    print(pred_array)
    pred_dataframe = pd.DataFrame(pred_array, columns = ['CO2EMISSIONS'])
    pred_dataframe = (pred_dataframe.astype(int))
    dataframe = pd.concat([data, pred_dataframe], axis=1)
    dataframe.to_csv('csv/prediction.csv', sep=',')

	
def encoder(data):
    le = preprocessing.LabelEncoder()
    for column_name in data.columns:
        if data[column_name].dtype == object:
            data[column_name] = le.fit_transform(data[column_name])
        else:
            pass

    return data 