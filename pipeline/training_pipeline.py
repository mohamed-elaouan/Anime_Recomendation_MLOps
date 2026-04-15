# from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining

from utils.common_functions import read_yaml
from config.paths_config import *

if __name__=="__main__":
    # data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    # data_ingestion.run()
    '''
    Data Ingestion is commented because the data ingestion is already done/ or handled using GCP bucket and the data is already available in the RAW_DIR.
    So we can directly move to data processing and model training steps.
    '''

    data_processor = DataProcessor(ANIMELIST_CSV,PROCESSED_DIR)
    data_processor.run()

    model_trainer = ModelTraining(PROCESSED_DIR)
    model_trainer.train_model()