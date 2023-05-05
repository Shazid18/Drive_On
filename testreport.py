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


# Test Case 2
try:
    report.write_step("Signup for a user", status=report.status.Start, test_number=2)

    driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/div/a/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[1]/input").send_keys("Orne")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[2]/input").send_keys("Israt")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[3]/input").send_keys("Jahan")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[4]/input").send_keys("orne@gmail.com")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[5]/input").send_keys("uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[6]/input").send_keys("uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[7]/input").click()
    time.sleep(2)
    assert (driver.title == 'Login')
    report.write_step('Successfully Signup.', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to Signup', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)


# Test Case 3
try:
    report.write_step('Login for a user', status=report.status.Start, test_number=3)

    driver.find_element(By.NAME, "username").send_keys("Shazid")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("Uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[3]/input").click()
    time.sleep(2)
    assert (driver.title == 'Home')
    report.write_step('Successfully login ', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to login', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 4
try:
    report.write_step('Rent Car', status=report.status.Start, test_number=4)

    driver.find_element(By.XPATH, "/html/body/ul/li[2]/a").click()
    time.sleep(2)
    assert (driver.title == 'Rent Car')
    report.write_step('Successfully redirect Rent Car page ', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to redirect Rent Car page', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

