import numpy as np

def n_size_ndarray_creation(n, dtype=np.int64):
    X = np.arange(n**2, dtype = dtype).reshape(n,n)
    return X

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int64):
    if type == 0:
        X = np.zeros(shape, dtype=dtype)
    elif type == 1:
        X = np.ones(shape, dtype)
    else:
        X = np.empty(shape, dtype)
    return X

def change_shape_of_ndarray(X, n_row):
    return X.reshape(n_row,-1)

def concat_ndarray(X_1, X_2, axis):
    pass

def get_n_largest_values(X, n):
    pass

#print(n_size_ndarray_creation(3, dtype=int))