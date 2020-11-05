#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This is the main function of the project
    from here we import the functions with the rest of the functionalities

    This is a building block for time series analysis

"""


from projectexample_dataloading import projectexample_dataloading
from projectexample_dataanalyse import projectexample_dataanalyse
from projectexample_modelling import projectexample_modelling
from projectexample_prediction import projectexample_prediction

import pandas as pd

def projectexample_main():
    """ Functionality0s main function description
    
        :params param1: this is a random parameter
        :type param1: float
        :params param2: this is second random parameter
        :type param: float
        :return:
            - error (int): variable with error code
            - output (type): Description
    """
    
    # initialize error (0: ok, 1: error)
    error = 0

    # define csv file name and separator
    file_name = "monthly-car-sales.csv"
    sep       = ","

    # 1 LOAD DATA
    series, error = projectexample_dataloading(file_name, sep)

    # 2 ANALYSE
    error = projectexample_dataanalyse(series)

    # 3 MODELLING
    # define model ARIMA, EXPS, SARIMA
    model ='SARIMAX'
    # define parameters SARIMAX: [p, d, q, P, D, Q, S, trend], ARIMA: [p,d,q], EXPS: [alfa]
    parameters = [1, 1, 1, 1, 1, 1, 1, 't']

    model_fitted, error = projectexample_modelling(series, model, parameters)

    # 4 FORECAST
    horizon = 24 # number of steps, hours, minutes, seconds
    yhat, error = projectexample_prediction(model_fitted, horizon)

    # 5 VISUALIZATION





    return error
        
    

if __name__ == '__main__':
    print('{} Start program'.format('-'*20))
    error = projectexample_main()