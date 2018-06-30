import numpy as np
import pandas as pd
from sklearn.externals import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def user_data_input():
    #take the input from user and return the values
    
def train_data(data):
    X=data.iloc[:,0:4]
    y=data.iloc[:,-1]
    X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.3, random_state=42)
    clf= RandomForestClassifier(n_estimators=13)
    clf.fit(X_train,y_train)
    # saving the trained model to the disk
    filename = 'finalized_model.sav'
    joblib.dump(clf, filename)
    # load the trained model from disk
    loaded_model = joblib.load(filename)
    #input ph, moisture, humidity, temperature
    ph_data,moisture_data,humidity_data,temperature_data= user_data_input(user_data)
    Xnew=[[ph_data,moisture_data,humidity_data,temperature_data]]
    y_pred_crop=loaded_model.predict(Xnew)
    ypreds=loaded_model.predict_proba(Xnew)
    ypred_prob=max(max(ypreds))
    if ypreds>0.5:
        #update the loaded model
        #dump the model
        return y_pred_crop,ypred_prob;
    
def main():
    data=pd.read_csv('datasets.csv')
    y_pred_crop,ypred_prob= train_data(data)
    print('Predicted crop',y_pred_crop)
    print('Prediction probability',ypred_prob)
    
if __name__=='__main__':
    main()