"""
nice functions through the bootcamp
"""
import numpy as np

def ecdf(data):
    """
    compute the x and y values needed to plot the ECDF
    (empirical cumulative distribution function)
    """
    x=np.sort(data)
    y=np.arange(0,1,1/len(x))
    return  x,y
