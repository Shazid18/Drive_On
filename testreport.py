from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pyhtmlreport import Report

driver = webdriver.Chrome(executable_path="E:\\UAP 3.2\\CSE 322\\Selenium\\chromedriver.exe")
driver.maximize_window()

report = Report()
report.setup(report_folder=r"E:\UAP 3.2\SSS\DriveOn\TestingReport", module_name="Report", release_name="release 1", selenium_driver=driver)


