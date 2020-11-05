#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This module fits the model

"""

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import os
from sklearn.metrics.regression import r2_score, mean_absolute_error, mean_squared_error
from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np


def projectexample_modelling(series, model_name, parameters):
    """ Function that performs the following plots
        shape of the series
        the first items

            :params series: univariate time series
            :type series: dataframe
            :return:
                - error (int): variable with error code
        """

    # modelling
    error = 0
    try:
        print("{} time series modelling".format('-' * 20))
        print("{} {} model".format('-' * 20, model_name))

        if model_name=='SARIMAX':

            p = parameters[0]
            d = parameters[1]
            q = parameters[2]
            P = parameters[3]
            D = parameters[4]
            Q = parameters[5]
            S = parameters[6]
            t = parameters[7]

            print("{} fitting model".format('-' * 20))
            # fit the model
            model = SARIMAX(series.values,
                             trend = t,
                             order = (p, d, q),
                             seasonal_order = (P, D, Q, S),
                             enforce_stationarity = False,
                             enforce_invertibility = False).fit()


            # Model summary
            print("{} Model summary".format('-' * 20))
            print(model.summary().tables[1])


            # Model diagnostic
            print("{} Model diagnostic".format('-' * 20))
            fig = model.plot_diagnostics(figsize=(20, 12))
            fig.savefig(os.path.join(os.getcwd(), 'figures\\diagnostic_{}.png'.format(model_name)))
            fig.show()

    except Exception as exception_msg:
        print('{} (!) Error in projectexample_modelling: '.format('-' * 20) + str(exception_msg))
        error = 1
        model = []
        return model, error

    # Metrics
    print("{} Metrics".format('-' * 20))
    try:
        # Regression metrics
        y_fitted = model.predict()
        R2 = round(r2_score(series, y_fitted), 3)
        MAE = round(mean_absolute_error(series, y_fitted), 3)
        RMSE = round(np.sqrt(mean_squared_error(series, y_fitted)), 3)

        print("{} R2: {}".format('-' * 20, R2))
        print("{} MAE: {}".format('-' * 20, MAE))
        print("{} RMSE: {}".format('-' * 20, RMSE))

    except Exception as exception_msg:
        print('{} (!) Error in projectexample_modelling (metrics): '.format('-' * 20) + str(exception_msg))
        error = 2
        return model, error




    return model, error