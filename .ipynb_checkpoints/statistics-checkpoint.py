import numpy as np 
import matplotlib.pyplot as plt 
class Statistics():
    def __init__(self, x:np.array, y:np.array):
        if(x.shape == y.shape):
            self.__x = x
            self.__y = y
            self.__xmean = np.mean(self.__x)
            self.__ymean = np.mean(self.__y)
    
    def __xdev(self):
        return self.__x - self.__xmean

    def __ydev(self):
        return self.__y - self.__ymean
    
    def regression(self):
        numerator = np.sum(self.__xdev()*self.__ydev())
        half_den = self.__xdev()**2
        denominator =  np.sum(half_den)
        m = numerator/denominator
        intercept = self.__ymean - m*self.__xmean
        return m, intercept

    def predictions(self, x_test:np.array):
        m, c = self.regression()
        ypred = m*x_test+c
        return ypred



if __name__ == '__main__':
    pass  


    
        