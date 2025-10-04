from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation import DataValidationTrainingPipeline
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

STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f"Stage {STAGE_NAME} started")
    obj = DataValidationTrainingPipeline()
    obj.initiate_data_validation()
    logger.info(f"Stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e