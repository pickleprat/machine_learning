import numpy as np 
import matplotlib.pyplot as plt 

class Statistics():
    def __init__(self, x:np.array, y:np.array):
        if(x.shape == y.shape):
            self.__x = x
            self.__y = y
            self.__xmean = np.mean(self.__x)
            self.__ymean = np.mean(self.__y)

        else: raise IndexError
        
    
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

    def peformance(self):
        ypred = self.predictions(self.__x)
        numerator = np.sum((self.__y - ypred)**2)
        denominator = np.sum((self.__y - self.__ymean)**2)
        return 1 - (numerator/denominator)
        



if __name__ == '__main__':
    import pandas as pd
    dataset = pd.read_csv('./archive/flat-prices.csv')
    x = dataset.iloc[:, 6]
    y = dataset.loc[:, 'resale_price']
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.75, random_state=0)
    st = Statistics(x_train, y_train)
    print(st.peformance())
    


    
        