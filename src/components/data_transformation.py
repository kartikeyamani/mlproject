import os
import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.utils import save_object
from src.exception import CustomException
from src.logger import logging

@dataclass
class Data_transformation_config:
    preprocessor_obj_file_path:str=os.path.join('artifacts','preprocessor.pkl')

class Data_Transformation:
    def __init__(self):
        self.data_tranformation_config=Data_transformation_config()
    def get_data_transformer_obj(self):
        '''
         This function returns the preporcessor object, when we do fit_transform on the data with this 
         preprocessor object then data tranformation happens and we can feed the data to model directly.
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehotencoder",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))
                ]
            )
            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
    
    def initiate_data_transformation(self,train_data_path,test_data_path):
        try:
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)

            logging.info("Train and test data read successfully")

            preprocessor_obj=self.get_data_transformer_obj()
            logging.info("Preprocessor objectt has been accessed")

            target_column="math_score"
            numerical_columns=["writing_score","reading_score"]

            train_df_input=train_data.drop(columns=[target_column],axis=1)
            train_df_target=train_data[target_column]

            test_df_input=test_data.drop(columns=[target_column],axis=1)
            test_df_target=test_data[target_column]

            logging.info("Test and Train Data is ready to be accessed.")
            train_arr_input=preprocessor_obj.fit_transform(train_df_input)
            test_arr_input=preprocessor_obj.transform(test_df_input)

            logging.info("Train and Test data is successfully preprocessed")

            train_arr=np.c_[
                train_arr_input,np.array(train_df_target)
            ]
            test_arr=np.c_[
                test_arr_input,np.array(test_df_target)
            ]
            save_object(

                file_path=self.data_tranformation_config.preprocessor_obj_file_path,
                obj=preprocessor_obj

            )
            return(
                train_arr,test_arr,self.data_tranformation_config.preprocessor_obj_file_path
            )


        except Exception as e:
            raise CustomException(e,sys)
