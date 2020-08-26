# CNN boilerplate - Advanced CNNs - Lazy Programmer - Udemy
# Input - Ryan L Buchanan 26AUG20

# Import numpy
import numpy as np

class MyModel:
    def predict(self, X):
        return X.dot(self.w)
    
    def fit(self, X, Y, eta, T):
        self.w = np.random.randn(x.shape[1])
        for i in range(T):
            Y_hat = self.predict(X)
            self.w = self.w - eta * X.T.dot(Y_hat - Y)

    def cost(self, X, Y):
        Y_hat = self.predict(X)
        return (Y_hat - Y).dot(Y_hat - Y)
    
X, Y = load_my_dataset()
model = MyModel()
model.fit(X, Y)