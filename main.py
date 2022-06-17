
from Classes.Plotting import Plotting
from Classes.Corelation import Corelation
from Classes.Predict import Predict
from Classes.Result import Result
if __name__ == "__main__":
    Plot=Plotting()
    data=Plot.Plot1()
    print(data.corr())
    Z=Corelation()
    x,y= Z.corelation(data)
    Q=Predict()
    S=Result()
    S.result(data)