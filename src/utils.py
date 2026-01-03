import os
import sys

import numpy as np 
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open (file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    


def evaluate_model(X_train, y_train, X_test, y_test, model, param):
    try:
        report = {}



        for i in range(len(list(model))):
            model_obj = list(model.values())[i]
            para = param[list(model.keys())[i]]



            gs = GridSearchCV(model_obj,para,cv=3)
            gs.fit(X_train,y_train)

            model_obj.set_params(**gs.best_params_)
            model_obj.fit(X_train, y_train)
            # Train model
            # model_obj.fit(X_train, y_train)

            # Predict
            y_Trian_pred = model_obj.predict(X_train)
            y_test_pred = model_obj.predict(X_test)

            # Score
            test_model_score = r2_score(y_test, y_test_pred)

            report[list(model.keys())[i]] = test_model_score
     

        return report

    except Exception as e:
        raise CustomException(e, sys)
