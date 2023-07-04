import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    """
    Any input that I require I give this class
    """
    train_data_path: str = os.path.join('datafolder',"train.csv")
    test_data_path: str = os.path.join('datafolder',"test.csv")
    raw_data_path: str = os.path.join('datafolder',"data.csv")


class DataIngestion:
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
    obj.initiate_data_ingestion()
