from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
logger.info("logger is working fine")
STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e