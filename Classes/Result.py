
class Result():
     def result(self,data):
         print(data)
         data.to_csv('Results/PredictedCADRate.csv', mode='a', index=False, header=False)
