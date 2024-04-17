import sys 
import os 
from src.exception import CustomException 

from src.logger import logging 
from src.utils import load_obj
from flask import Flask, request, render_template
import pandas as pd

class PredictPipeline: 
    def __init__(self) -> None:
        pass

    def predict(self, features): 
        try: 
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join("artifacts", "model.pkl")

            preprocessor = load_obj(preprocessor_path)
            model = load_obj(model_path)

            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e: 
            logging.info("Error occured in predict function in prediction_pipeline location")
            raise CustomException(e,sys)
        
class CustomData: 
        def __init__(self, Name:str, 
                     Mileage:float, 
                     Year:float,
                     Kms_Driven:float,
                     FuelType:str, 
                     Gearbox:str, 
                     ): 
                self.Name =Name
                self.Mileage =Mileage
                self.Year = Year
                self.Kms_Driven=Kms_Driven
                self.FuelType =FuelType
                self.Gearbox = Gearbox
              
               
        def get_data_as_dataframe(self): 
            try: 
                custom_data_input_dict = {
                    'Name': [self.Name], 
                    'Mileage': [self.Mileage],
                    'Year': [self.Year], 
                    'Kms_Driven': [self.Kms_Driven],
                    'FuelType':[self.FuelType],
                    'Gearbox':[self.Gearbox], 
                   
                }
                
                df = pd.DataFrame(custom_data_input_dict)
                logging.info("Dataframe created")
                return df
            except Exception as e:
                logging.info("Error occured in get_data_as_dataframe function in prediction_pipeline")
                raise CustomException(e,sys) 
             
             
        