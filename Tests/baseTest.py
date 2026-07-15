from datetime import datetime

import pytest

from utils.logger import Logger


@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class baseTest():
    logger = Logger.get_logger()