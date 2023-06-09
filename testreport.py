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

# Test Case 5
try:
    report.write_step('Rent Car Booking', status=report.status.Start, test_number=5)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/a").click()
    time.sleep(2)
    assert (driver.title == 'Booking Details')
    report.write_step('Successfully redirect Rent Car Booking page ', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to redirect Rent Car Booking page', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 6
try:
    report.write_step('Buy Car', status=report.status.Start, test_number=6)

    driver.find_element(By.XPATH, "/html/body/ul/li[3]/a").click()
    time.sleep(2)
    assert (driver.title == 'Buy Car')
    report.write_step('Successfully redirect Buy Car page ', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to redirect Buy Car page', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 7
try:
    report.write_step('Buy Car Details', status=report.status.Start, test_number=7)

    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[1]/div/a").click()
    time.sleep(2)
    assert (driver.title == 'Car Details')
    report.write_step('Successfully redirect Buy Car Details page ', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to redirect Buy Car Details page', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 8
try:
    report.write_step('Payment', status=report.status.Start, test_number=8)

    driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/a").click()
    time.sleep(2)
    assert (driver.title == 'Buy Car Payment')
    report.write_step('Payment Successfull', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Payment Failed', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 9
try:
    report.write_step('Hire Driver', status=report.status.Start, test_number=9)

    driver.find_element(By.XPATH, "/html/body/ul/li[4]/a").click()
    time.sleep(2)
    assert (driver.title == 'Hire Driver')
    report.write_step('Successfully redirect Hire Driver page', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to redirect Hire Driver page', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 10
try:
    report.write_step('Goto to Profile', status=report.status.Start, test_number=10)

    driver.find_element(By.XPATH, "/html/body/ul/li[5]/a").click()
    time.sleep(2)
    assert (driver.title == 'Profile')
    report.write_step('Profile loded Successfully', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to load Profile', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 11
try:
    report.write_step('Update Profile', status=report.status.Start, test_number=11)

    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/div/div[10]/div/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[1]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[1]/input").send_keys("Ahmed")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[2]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[2]/input").send_keys("Shamir")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[6]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[6]/input").send_keys("01796221385")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[7]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[7]/input").send_keys("159753258")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[8]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[8]/input").send_keys("Mirpur-1")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[9]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[9]/input").send_keys("Dhaka")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[10]/input").clear()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/fieldset/p[10]/input").send_keys("1206")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/div/button").click()
    time.sleep(2)
    assert (driver.title == 'Profile')
    report.write_step('Profile Update Successfully', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to Update Profile', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 12
try:
    report.write_step('Update Password', status=report.status.Start, test_number=12)

    driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[1]/div/div/div/div[2]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/p[1]/input").send_keys("Uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/p[2]/input").send_keys("uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/p[3]/input").send_keys("uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/form/button").click()
    time.sleep(2)
    assert (driver.title == 'Profile')
    report.write_step('Password Update Successfully', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to Update Password', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 13
try:
    report.write_step('Logout User', status=report.status.Start, test_number=13)

    driver.find_element(By.XPATH, "/html/body/ul/li[10]/a").click()
    time.sleep(2)
    assert (driver.title == 'Home:DriveOn')
    report.write_step('User has been logged out.', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to Logout', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)

# Test Case 14
try:
    report.write_step('Login user with updated password', status=report.status.Start, test_number=14)

    driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/a").click()
    time.sleep(1)
    driver.find_element(By.NAME, "username").send_keys("Shazid")
    time.sleep(2)
    driver.find_element(By.NAME, "password").send_keys("uap12345")
    time.sleep(2)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/form/div[3]/input").click()
    time.sleep(2)
    assert (driver.title == 'Home')
    report.write_step('Successfully login with updated password', status=report.status.Pass, screenshot=True)

except AssertionError:
    report.write_step('Failed to login with updated password', status=report.status.Fail, screenshot=True)

except Exception as e:
    report.write_step('Something went wrong!!!', status=report.status.Warn, screenshot=True)



finally:
    report.generate_report()

driver.close()