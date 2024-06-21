import numpy as np
if __name__ == '__main__':
    Z = np.random.randint(0,5,(10,10))
    n = 3
    i = 1 + (Z.shape[0]-3)
    j = 1 + (Z.shape[1]-3)
    C = np.lib.stride_tricks.as_strided(Z, shape=(i, j, n, n), strides=Z.strides + Z.strides)
    print (C)
