from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pyhtmlreport import Report

driver = webdriver.Chrome(executable_path="E:\\UAP 3.2\\CSE 322\\Selenium\\chromedriver.exe")
driver.maximize_window()

report = Report()
report.setup(report_folder=r"E:\UAP 3.2\SSS\DriveOn\TestingReport", module_name="Report", release_name="release 1", selenium_driver=driver)


# Test Case 1
try:
    report.write_step("Goto Index Page", status=report.status.Start, test_number=1)

    driver.get("http://127.0.0.1:8000")
    time.sleep(2)
    assert (driver.title == 'Home:DriveOn')
    report.write_step('Index Page loaded Successfully.', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Index Page loaded Failed.', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)


