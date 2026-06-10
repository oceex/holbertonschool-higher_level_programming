#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return[*map(lambda x:[*map(lambda w:w*w,x)]if type(x)==list else x*x,matrix)]
