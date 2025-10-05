from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer

from src.datascience import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_training(self):
        config = ConfigurationManager()
        Model_trainer_config = config.get_model_trainer_config()
        Model_trainer_config = ModelTrainer(config=Model_trainer_config)
        Model_trainer_config.train()
        
if __name__ == '__main__':
    try:
        logger.info(f"Stage {STAGE_NAME} started")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f"Stage {STAGE_NAME} completed")
    except Exception as e:
        logger.exception(e)
        raise e