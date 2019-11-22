import numpy as np


def softmax(inMatrix):
    m, n = np.shape(inMatrix)
    outMatrix = np.mat(np.zeros((m, n)))
    soft_num = 0
    for i in range(0, n):
        outMatrix[0, i] = np.exp(inMatrix[0, i])
        soft_num += outMatrix[0, i]
    for i in range(0, n):
        outMatrix[0, i] = outMatrix[0, i]/soft_num
    return outMatrix


a = np.array([[1, 2, 1, 2, 1, 1, 3]])
b = softmax(a)
print(b)



