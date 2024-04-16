import lib
import logging
from logging import INFO

if __name__ == "__main__":
  logging.basicConfig(filename = "main.log", level = INFO)

  logger = logging.getLogger(__name__)
  logger.info("START")
  lib.write_log()
  logger.info("END")
