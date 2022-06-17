import numpy as np
import pandas as pnd
import matplotlib.pyplot as plot
import seaborn as seb
from seaborn import regression
class Plotting:
    def Plot1(self):
        seb.set()
        plot.style.use('seaborn-whitegrid')
        data = pnd.read_csv("USD-CAD=X.csv")
        print(data.head())
        plot.figure(figsize=(15, 6))
        plot.title("USD - CAD Exchange Rate")
        plot.xlabel("Date")
        plot.ylabel("Close")
        plot.plot(data["Close"])
        plot.savefig("Results/USD-CAD.png")
        return data