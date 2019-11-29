from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Make sure you have selenium driver and firefox browser installed and added to path
# Works with amazon/flipkart india
# Enter product URL, Account ID, Password to below variables

product_url = "URL"
my_id = "Email/MobileNo."
my_pwd = "Password"

def set_site(url):
	if "amazon" in url:
		amazon(url)
	elif "flipkart" in url:
		flipkart(url)
	else:
		raise TypeError("Invalid URL: Sorry, this script only supports Amazon and Flipkart!")

def amazon(url):
	browser = webdriver.Firefox()
	browser.get(url)
	browser.find_element_by_id("buy-now-button").click()
	browser.find_element_by_id("ap_email").send_keys(my_id)
	browser.find_element_by_id("continue").click()
	browser.find_element_by_id("ap_password").send_keys(my_pwd)
	browser.find_element_by_id("signInSubmit").click()

def flipkart(url):
	browser = webdriver.Firefox()
	browser.get(url)
	browser.find_element(By.XPATH, '//button[text()="BUY NOW"]').click()
	sleep(2)
	browser.find_element_by_xpath("//div[@class='_6Ip9N2']/form/div/input").send_keys(my_id)
	browser.find_element_by_xpath('//button/span[text()="CONTINUE"]').click()
	browser.find_element_by_xpath('//input[@type="password"]').send_keys(my_pwd)
	browser.find_element_by_xpath('//button/span[text()="Login"]').click()

set_site(product_url)
