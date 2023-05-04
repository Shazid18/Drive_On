from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="E:\\UAP 3.2\\CSE 322\\Selenium\\chromedriver.exe")
driver.maximize_window()

#Index page
driver.get("http://127.0.0.1:8000")
time.sleep(2)


# #Clicking signupbutton
# driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/div/a/button").click()
# time.sleep(2)

# #signup button test
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[1]/input").send_keys("Lia")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[2]/input").send_keys("Radia")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[3]/input").send_keys("Rahman")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[4]/input").send_keys("Lia@gmail.com")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[5]/input").send_keys("uap12345")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/div[6]/input").send_keys("uap12345")
# time.sleep(2)
# driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/form/div[7]/input").click()
# time.sleep(2)



#clicking login button
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/a").click()
time.sleep(1)


#login
driver.find_element(By.NAME, "username").send_keys("Shazid")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("Uap12345")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[3]/input").click()
time.sleep(2)


#going to rent car list
driver.find_element(By.XPATH,"/html/body/ul/li[2]/a").click()
time.sleep(2)

#seeing rent car booking details
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div/a").click()
time.sleep(2)

#going to buy car list
driver.find_element(By.XPATH,"/html/body/ul/li[3]/a").click()
time.sleep(2)

#seeing buy car  details
driver.find_element(By.XPATH,"/html/body/div[3]/div/div/div[1]/div/a").click()
time.sleep(2)

#confirm buy car payment
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/a").click()
time.sleep(2)

# #get transiction Id
# driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/form/div/div[1]/div/input").send_keys("54ff51f6")
# time.sleep(2)
# driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/form/div/div[2]/button").click()
# time.sleep(2)

#going to hire driver page
driver.find_element(By.XPATH,"/html/body/ul/li[4]/a").click()
time.sleep(2)

#going to driver payment page
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/a").click()
time.sleep(2)

#going to profile page
driver.find_element(By.XPATH,"/html/body/ul/li[5]/a").click()
time.sleep(2)

#going to profile edit page
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/div/div[10]/div/a").click()
time.sleep(2)

#updating profile
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
driver.find_element(By.XPATH,"/html/body/div[2]/form/div/button").click()
time.sleep(2)


#going to update password
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[1]/div/div/div/div[2]/a").click()
time.sleep(2)

#update password
driver.find_element(By.XPATH, "/html/body/div[2]/form/p[1]/input").send_keys("Uap12345")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/form/p[2]/input").send_keys("Uap12345")
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[2]/form/p[3]/input").send_keys("Uap12345")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/form/button").click()
time.sleep(2)

#going to home page by clicking icon
driver.find_element(By.XPATH,"/html/body/div[1]/a/img").click()
time.sleep(2)

#logout
driver.find_element(By.XPATH,"/html/body/ul/li[10]/a").click()
time.sleep(2)

#login with updated password
driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/a").click()
time.sleep(1)
driver.find_element(By.NAME, "username").send_keys("Shazid")
time.sleep(2)
driver.find_element(By.NAME, "password").send_keys("Uap12345")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/form/div[3]/input").click()
time.sleep(2)





driver.close()