import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://127.0.0.1:5001")
time.sleep(2)
def main():
    read()
    create()
    fetch()
    update()
    fetch()
    delete()
def read():
    driver.find_element(By.ID, "readButton").click()
    time.sleep(5)
def create():
    driver.find_element(By.ID, "createButton").click()
    driver.find_element(By.ID, "createName").send_keys("avinash")
    driver.find_element(By.ID, "createDoj").send_keys("20-09-2022")
    driver.find_element(By.ID, "createLocation").send_keys("Vijayawda")
    driver.find_element(By.ID, "createProject").send_keys("CISCO")
    driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
    time.sleep(5)
def fetch():
    driver.find_element(By.ID, "fetchButton").click()
    driver.find_element(By.ID, "fetchEmployeeId").send_keys('1')
    driver.find_element(By.XPATH, "(//button[@type='submit'])[2]").click()
    time.sleep(5)

def update():
    driver.find_element(By.ID, "updateButton").click()
    driver.find_element(By.ID, "updateEmployeeId").send_keys("2")
    driver.find_element(By.XPATH, "(//button[@type='submit'])[3]").click()
    driver.find_element(By.ID, "updateName").clear()
    driver.find_element(By.ID, "updateName").send_keys("AVINASH")
    driver.find_element(By.ID, "updateDoj").clear()
    driver.find_element(By.ID, "updateDoj").send_keys("20-09-2022")
    driver.find_element(By.ID, "updateLocation").clear()
    driver.find_element(By.ID, "updateLocation").send_keys("NODIA")
    driver.find_element(By.ID, "updateProject").clear()
    driver.find_element(By.ID, "updateProject").send_keys("CISCO")
    driver.find_element(By.XPATH, "(//button[@type='submit'])[4]").click()
    driver.find_element(By.ID, "fetchButton").click()
    driver.find_element(By.ID, "fetchEmployeeId").clear()
    time.sleep(5)
def delete():
    driver.find_element(By.ID, "deleteButton").click()
    driver.find_element(By.ID, "deleteEmployeeId").send_keys("1")
    driver.find_element(By.XPATH, "(//button[@type='submit'])[5]").click()
    driver.find_element(By.ID, "fetchButton").click()
    driver.find_element(By.ID, "readButton").click()
    time.sleep(5)
    print("Test passed")
    driver.quit()

if __name__ == "__main__":
    main()
