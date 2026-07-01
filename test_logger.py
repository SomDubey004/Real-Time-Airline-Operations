from utils.logger import get_logger

logger = get_logger()

logger.info("Pipeline started successfully.")
logger.warning("This is a sample warning.")
logger.error("This is a sample error.")

print("Logger test completed!")