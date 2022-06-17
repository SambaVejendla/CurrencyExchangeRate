
from Classes.Plotting import Plotting
from Classes.Corelation import Corelation
from Classes.Predict import Predict
from Classes.Result import Result
if __name__ == "__main__":
    Plot=Plotting()
    data=Plot.Plot1()
    print(data.corr())
    Cor=Corelation()
    x,y= Cor.corelation(data)
    pdt=Predict()
    Prdt=pdt.predict(x,y)
    Final=Result()
    Final.result(Prdt)