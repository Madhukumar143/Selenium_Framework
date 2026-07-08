from datetime import datetime

import pytest

from utils.logger import Logger


@pytest.mark.usefixtures("setup_and_teardown","log_on_result")
class baseTest():

    def logger(self):
        return Logger.get_logger(self.__class__.__name__)
