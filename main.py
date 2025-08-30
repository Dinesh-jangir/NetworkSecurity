from NetworkSecurity.components.data_ingestion import DataIngestion
from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging 
from NetworkSecurity.entity.config_entity import DataIngestionConfig ,TrainingPipelineConfig 
import sys

if __name__=="__main__":
    try:

        train_pipe_line_config = TrainingPipelineConfig()

        data_ingestion_confit  =  DataIngestionConfig(train_pipe_line_config)

        data_ingestion = DataIngestion(data_ingestion_confit)

        logging.info("Initiate the data Ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        print(data_ingestion_artifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)