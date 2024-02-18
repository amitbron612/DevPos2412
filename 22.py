from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.get("C:/Users/AMITB/Downloads/tip_calc/tip_calc/index.html")
billamt = dr.find_element(by="id", value="billamt")
billamt.send_keys("100")
dr.find_element(by="xpath", value="/html/body/div/div[1]/form/p[4]/select/option[3]").click()
dr.find_element(by="id", value="peopleamt").send_keys("5")
dr.find_element(by="id", value="musicamt").send_keys("5")
dr.find_element(by="id", value="calculate").click()
actual = dr.find_element(by="id", value="tip").text
expected = "9"
assert actual == expected

sleep(30)