#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    This is the main function of the project
    from here we import the functions with the rest of the functionalities

"""

def projectexample_main(param1, param2):
    """ Functionality0s main function description
    
        :params param1: this is a random parameter
        :type param1: float
        :params param2: this is second random parameter
        :type param: float
        :return:
            - error (int): variable with error code
            - output (type): Description
    """
    
    # initialize error
    error=0
    
    
    try:
        print("Part #1: Auxiliar functionality code ")
        output = param1 + param2
    except Exception as exception_msg:
        print('(!) Error in project_name_functionality_part1' + str(exception_msg) )
        output = []
        error = 1
        return(error, output)
    
     try:
        print("Part #2: Auxiliar functionality code ")
        output = output**(param1+param2)
    except Exception as exception_msg:
        print('(!) Error in project_name_functionality_part2' + str(exception_msg) )
        output = []
        error = 2
        return(error, output)
    
    
     try:
        print("Part #3: Auxiliar functionality code ")
        output = output**2 + output**(1/3)
    except Exception as exception_msg:
        print('(!) Error in project_name_functionality_part3' + str(exception_msg) )
        output = []
        error = 3
        return(error, output)
        
    

if __name__ == '__main__':
    a = 1
    b = 3
    projectexample_main(a, b)