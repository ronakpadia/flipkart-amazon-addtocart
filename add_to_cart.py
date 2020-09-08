from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

# Make sure you have selenium driver and firefox browser installed and added to path
# Works with amazon/flipkart india
# Enter product URL, Account ID, Password to below variables
# This script will only add the product to your cart and take you to the payment page

product_url = "URL"
my_id = "Email/MobileNo."
my_pwd = "Password"
browser = webdriver.Firefox()
# Set the time of flash sale here! 
buy_time = datetime(2020, 9, 8, 14, 18, 0000000) # (Year, Month, Day, Hour, Minute, Milisecond)

def set_site():
	if "amazon" in product_url:
		amazon_sign_in()
		return "amazon"
	elif "flipkart" in product_url:
		flipkart_sign_in()
		return "flipkart"
	else:
		raise TypeError("Invalid URL: Sorry, this script only supports Amazon and Flipkart!")

def amazon_sign_in():
	browser.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fcss%2Fhomepage.html%3Ffrom%3Dhz%26ref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
	browser.find_element_by_id("ap_email").send_keys(my_id)
	browser.find_element_by_id("continue").click()
	browser.find_element_by_id("ap_password").send_keys(my_pwd)
	browser.find_element_by_id("signInSubmit").click()
	print("PLEASE APPROVE YOUR AMAZON SIGN IN FROM TRUSTED DEVICE!")
	print("WAIT FOR THE SALE TO START!")

def amazon_buy_now(url):
	browser.get(url)
	browser.find_element_by_id("buy-now-button").click()

def flipkart_sign_in():
	browser.get("https://www.flipkart.com/account/login")
	browser.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/input").send_keys(my_id)
	browser.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[2]/input').send_keys(my_pwd)
	browser.find_element_by_xpath('//button/span[text()="Login"]').click()

def flipkart_buy_now(url):
	browser.get(url)
	browser.find_element(By.XPATH, '//button[text()="BUY NOW"]').click()

site = set_site()

while True:
	now = datetime.now()
	if now > buy_time:
		if site == "amazon":
			amazon_buy_now(product_url)
		if site == "flipkart":
			flipkart_buy_now(product_url)
		break
