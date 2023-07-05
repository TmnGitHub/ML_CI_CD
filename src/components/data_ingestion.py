import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    """
    Any input that I require I give this class
    """
    train_data_path: str = os.path.join('datafolder',"train.csv")
    test_data_path: str = os.path.join('datafolder',"test.csv")
    raw_data_path: str = os.path.join('datafolder',"data.csv")


class DataIngestion:

    """ 
    Description:
    This class is responsible for initiating the data ingestion process. 
    It reads data from a specified source, performs preprocessing steps, and splits the data into training and testing sets. 
    The processed data is then saved in the respective locations specified in the ingestion configuration.

    Parameters:
    None

    Returns:
    A tuple containing the paths to the training and testing data files.

    Exceptions:
    If any error occurs during the data ingestion process, a CustomException is raised with the corresponding error message and the sys module.

    Example Usage:
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    """
    def __init__(self):
        self.ingestion_config =  DataIngestionConfig() #Composition: class Composite can contain an object of another class Component

    def initiate_data_ingestion(self):
        """
        if the data is stored in some place. the code will be writtern here to read from database,...

        """
        logging.info("Entered the data ingestion method")

        try:
            df=pd.read_csv('Data/stud.csv') # read it from local machine
            logging.info('Imported the dataset as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion complete")

            return(
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path
            )

        except Exception as e:

            raise CustomException(e,sys)

            

if __name__ == "__main__":
    obj=DataIngestion()
    train_data_path,test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr,test_arr,preprocessor_file_path = data_transformation.initate_data_transformation(train_data_path,test_data_path )

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr,preprocessor_file_path ))

