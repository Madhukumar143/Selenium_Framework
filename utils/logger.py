import logging
import os
import sys


""""class Logger:
    @staticmethod
    def get_logger(name):

        log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        log_file = os.path.join(log_dir, "test_log.log")

        os.makedirs(log_dir, exist_ok=True)

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        if logger.hasHandlers():
            logger.handlers.clear()

        # File handler
        fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

        logger.addHandler(fh)
        logger.addHandler(ch)

        logger.propagate = False

        return logger
"""

import logging
import os
import sys
from datetime import datetime


class Logger:
    @staticmethod
    def get_logger(name):

        # Create logs folder path
        log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
        os.makedirs(log_dir, exist_ok=True)

        # Log file path (single file - append mode)
        log_file = os.path.join(log_dir, "test_log.log")

        # Create logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        # Avoid duplicate logs
        if logger.hasHandlers():
            logger.handlers.clear()

        # File handler (APPEND mode)
        fh = logging.FileHandler(log_file, mode="w", encoding="utf-8")
        fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))

        # Console handler
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))

        # Add handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

        # Prevent duplicate logs from root logger
        logger.propagate = False

        # Add separator for each test run (optional but useful)
        logger.info("\n========== NEW TEST RUN ==========\n")

        return logger