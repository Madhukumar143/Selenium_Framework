# Ensure project root is on sys.path so local packages (like `utils`) are importable
import pyautogui
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utils.logger import Logger
from utils import ReadConfigurations


@pytest.fixture(scope="session", autouse=True)
def logger():
    # lazy import to avoid ModuleNotFoundError at import time

    logger = Logger.get_logger("PytestFramework")
    logger.info("Starting Test Execution")
    yield logger
    logger.info("Ending Test Execution")

@pytest.fixture()
def log_on_result(request):
    yield
    item = request.node
    if item.rep_call.failed or item.rep_call.outcome == 'failed':
        # Capture for any failure, including assertion errors
        # Capture screenshot for failed case (including assertion failures)
        allure.attach(driver.get_screenshot_as_png(), name="Failed_Screenshot", attachment_type=AttachmentType.PNG)
    else:
        # Attach screenshot for passed test cases
        allure.attach(driver.get_screenshot_as_png(), name="Passed_Screenshot", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture() # we can use autouse, scope as parameters here
def setup_and_teardown(request):
    # lazy import of ReadConfigurations so import happens when fixtures run
    browser = ReadConfigurations.read_configuration("basic info", "browser") #chrome
    global driver
    driver = None

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name")
    driver.maximize_window()
    driver.implicitly_wait(2)
    cur_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(cur_url)
    # Perform zoom-out (Ctrl + -) 3 times
    for _ in range(4):
        pyautogui.hotkey('ctrl', '-')  # Simulate Ctrl and - keypress together
    request.cls.driver = driver
    yield
    driver.quit()