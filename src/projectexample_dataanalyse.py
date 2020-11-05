#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This is the main module to load data

"""

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import os
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


def projectexample_dataanalyse(series):
    """ Function that performs the following plots
        shape of the series
        the first items

            :params series: univariate time series
            :type series: dataframe
            :return:
                - error (int): variable with error code
        """

    error = 0

    try:
        print("{} Shape of the time series data set:{}".format('-' * 20, series.shape))
        print("{} Print first values: ".format('-' * 20))
        print(series.head())

        print("{} Plot time series".format('-' * 20))
        plt.figure(figsize=(20,12))
        plt.plot(series.index, series.values)
        plt.savefig(os.path.join(os.getcwd(), 'figures\\timeseries_plot.png'))
        plt.show()

        print("{} Plot autocorrelation function".format('-' * 20))
        fig = plot_acf(series)
        fig.savefig(os.path.join(os.getcwd(), 'figures\\acf_plot.png'))
        fig.show()

        print("{} Plot partial-autocorrelation function".format('-' * 20))
        fig = plot_pacf(series)
        fig.savefig(os.path.join(os.getcwd(), 'figures\\pacf_plot.png'))
        fig.show()

    except Exception as exception_msg:
        print('{} (!) Error in projectexample_dataanalyse: '.format('-' * 20) + str(exception_msg))
        error = 1
        return output, error



    return error