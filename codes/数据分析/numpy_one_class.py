import numpy as np
def svd(np_data):
    U, S, V = np.linalg.svd(np_data) # Singular Value Decomposition
    rank = np.sum(S > 1e-10)
    print(rank)



if __name__ == '__main__':
    data = np.random.uniform(0,1,(10,10))
    svd(data)