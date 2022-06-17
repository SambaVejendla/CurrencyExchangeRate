import numpy as np
import pandas as pnd
import matplotlib.pyplot as plot
import seaborn as seb
from seaborn import regression

class Corelation():
    def corelation(self,data):
         seb.heatmap(data.corr())
         plot.savefig("Results/Heatmap.png")
         x = data[["Open", "High", "Low"]]
         y = data["Close"]
         x = x.to_numpy()
         y = y.to_numpy()
         y = y.reshape(-1, 1)
         return x,y
