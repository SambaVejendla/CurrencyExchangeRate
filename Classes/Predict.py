import pandas as pnd
import seaborn as seb
from seaborn import regression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

class Predict():
    def predict(self,x,y):
        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)
        model = DecisionTreeRegressor()
        model.fit(xtrain, ytrain)
        ypred = model.predict(xtest)
        data = pnd.DataFrame(data={"Predicted Rate": ypred.flatten()})
        return data