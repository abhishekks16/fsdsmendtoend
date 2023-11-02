import pandas as pd
import numpy as np
import os
import sys

from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exception import customException

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path



class DataIngestionConfig:
    #artifact_path = os.path.join(os.getcwd(),"artifacts")
    raw_data_path : str = os.path.join("artifacts","raw.csv")
    train_data_path : str = os.path.join("artifacts","train.csv")
    test_data_path : str = os.path.join("artifacts","test.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")

        try:
            logging.info(f"Dataset reading is started")
            data = pd.read_csv(Path(os.path.join("notebooks/data", "gemstone.csv")))
            logging.info(f"Dataset reading is completed with data shape : {data.shape}")

            logging.info("Saving raw data into the artifacts")
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok = True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Splitting the data for Train and Test started")
            train_data, test_data = train_test_split(data, test_size=0.25)

            logging.info("Saving train data into the artifacts")
            train_data.to_csv(self.ingestion_config.train_data_path, index = False)

            logging.info("Saving test data into the artifacts")
            test_data.to_csv(self.ingestion_config.test_data_path, index = False)

            logging.info("Splitting the data for Train and Test completed")

            # returing the train and test data path
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Exception occoured during data ingestion stage")
            raise customException(e, sys)
