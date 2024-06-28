import joblib

class Model:
  model = None
  
  def __init__(self, path:str):
   self.model= self.load_model(path)

  def load_model(self, path:str):
    try:
      return joblib.load(path)
    except Exception as ee:
      return None, "Model not loaded"
  
  def tokenize(self, text):
    if(self.model):
      return self.model.tokenize(text)
    else:
      return "Model not loaded"
  
model1 = Model("D:/CRATIC_PLN_UNIM/CLASE_1/backend/models/model2.pkl")
model2 = Model("D:/CRATIC_PLN_UNIM/CLASE_1/backend/models/model2.pkl")
model3 = Model("D:/CRATIC_PLN_UNIM/CLASE_1/backend/models/model3.pkl")
model4 = Model("D:/CRATIC_PLN_UNIM/CLASE_1/backend/models/model4.pkl")
model5 = Model("D:/CRATIC_PLN_UNIM/CLASE_1/backend/models/model5.pkl")