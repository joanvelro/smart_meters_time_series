#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This is the main module to load data

"""
import pandas as pd
import os

def projectexample_dataloading(file_name, sep):
    """ Function to load the dataset from a local storage unit
    
        :params param1: path to the dataset
        :type param1: string
        :return:
            - error (int): variable with error code
            - output (type): dataframe
    """
    
    # initialize error
    error = 0
    
    try:

        # move up one directory (from src to project folder level)
        os.chdir("..")
        # set current directory as the directory of the data to load the data
        os.chdir(os.path.join(os.getcwd(), 'data\\'))

        print("{} Data Loading from single csv file".format('-'*20))
        output = pd.read_csv(file_name, sep=sep, header=0, index_col=0)

        # move up one directory again (from data to project folder level)
        os.chdir("..")

        # format index to datetime format
        output.index = pd.to_datetime(output.index)

        return output, error
    except Exception as exception_msg:
        print('{} (!) Error in projectexample_dataloading: '.format('-'*20) + str(exception_msg) )
        output = []
        error  = 1
        return output, error
    
    
        
