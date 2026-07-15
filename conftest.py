import os
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from utils import ReadConfigurations
from utils.ReadConfigurations import get_url  # ← add this import
from utils.logger import Logger
import logging

@pytest.fixture(scope="session", autouse=True)
def logger():
    
    logger = Logger.get_logger()
    logger.info("STARTING TEST EXECUTION")
    logger.info("=" * 50)

    yield logger

    logger.info("=" * 50)
    logger.info("ENDING TEST EXECUTION")
    logging.shutdown()

@pytest.fixture()
def log_on_result(request):
    yield
    item = request.node
    if item.rep_call.failed or item.rep_call.outcome == 'failed':
        allure.attach(driver.get_screenshot_as_png(), name="Failed_Screenshot", attachment_type=AttachmentType.PNG)
    else:
        allure.attach(driver.get_screenshot_as_png(), name="Passed_Screenshot", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    global driver
    options = webdriver.ChromeOptions()

    if os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--remote-debugging-port=9222")

    if browser.__eq__("chrome"):
        driver = webdriver.Chrome(options=options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox(options=options)
    elif browser.__eq__("edge"):
        driver = webdriver.Edge(options=options)
    else:
        print("Provide a valid browser name")

    driver.implicitly_wait(2)
    driver.set_page_load_timeout(30)

    cur_url = get_url()  # ← only change — reads UAT or SIT url based on config

    try:
        driver.get(cur_url)
    except Exception as e:
        print(f"Failed to load URL: {cur_url} — Site may be down. Error:")
        driver.quit()
        raise

    if os.getenv("GITHUB_ACTIONS") != "true":
        driver.maximize_window()
        driver.execute_script("document.body.style.zoom='75%'")

    request.cls.driver = driver

    yield

    try:
        driver.quit()
    except Exception as e:
        print(f"Error during driver quit:")