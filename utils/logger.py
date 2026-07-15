import logging
import os
import sys
from datetime import datetime


class Logger:
    _logger = None

    @staticmethod
    def get_logger():

        # Return existing logger
        if Logger._logger:
            return Logger._logger

        # Project Root
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Logs Folder
        log_folder = os.path.join(project_root, "logs")
        os.makedirs(log_folder, exist_ok=True)

        # Log File Name
        log_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".log"
        log_file = os.path.join(log_folder, log_name)

        # ---------------- WRITE HEADER ---------------- #

        with open(log_file, "w", encoding="utf-8") as file:

            file.write("=" * 140 + "\n")
            file.write("{:^140}\n".format("SELENIUM AUTOMATION EXECUTION LOG"))
            file.write("=" * 140 + "\n")

            file.write(
                "{:<19} |{:<9} |{:<26} |{:<36} |{}\n".format(
                    "DATE & TIME",
                    "LEVEL",
                    "MODULE",
                    "FUNCTION",
                    "MESSAGE"
                )
            )

            file.write("-" * 140 + "\n")

        # ------------------------------------------------ #

        logger = logging.getLogger("Framework")
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(module)-25s | %(funcName)-35s | %(message)s",datefmt="%d-%m-%Y %H:%M:%S"
        )

        # File Handler
        file_handler = logging.FileHandler(
            log_file,
            mode="a",
            encoding="utf-8"
        )

        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Console Handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)

        console_handler.setFormatter(
            logging.Formatter("%(levelname)s | %(message)s")
        )

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        logger.propagate = False

        Logger._logger = logger

        return logger