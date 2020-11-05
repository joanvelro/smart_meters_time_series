#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This module allows to perform the prediction based on the trained models
"""

def projectexample_prediction(model_fitted, forecast_steps):
    """ Funtion to perform the foreast with the time series model trained
    
        :params model: time series model trained
        :type param1: model
        :params param2: number of steps ahead to forecast
        :type param: integer
        :return:
            - error (int): variable with error code
            - output (array): array with the forecast
    """
    
    # initialize error
    error = 0
    
    try:
        print("{} Forecasting".format('-'*20))
        yhat   = model_fitted.forecast(forecast_steps)

    except Exception as exception_msg:
        print('{} (!) Error in projectexample_prediction'.format('-'*20) + str(exception_msg) )
        yhat = []
        error  = 1
        return(error, output)

    return yhat, error
    
    
        