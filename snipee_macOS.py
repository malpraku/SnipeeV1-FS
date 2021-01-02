# Halo ngab, jangan skid skid yaa :/.

from time import gmtime, strftime
from random import randint
import subprocess
import pathlib
import ctypes
import time
import os
import datetime

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print("Mengecek beberapa module penting untuk program ini, harap tunggu.")
try:
    from discord_webhook import DiscordWebhook
    print("[discord_webhook] found, searching others...")
except ModuleNotFoundError:
	print("[discord_webhook] not found, installing...")
	install(discord_webhook)
	pass
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC    
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import TimeoutException
    print("[selenium] found, searching others...")
except ModuleNotFoundError:
	print("[selenium] not found, installing...")
	install(selenium)
	pass
try:
    import requests
    print("[requests] found, searching others...")
except ModuleNotFoundError:
	print("[requests] not found, installing...")
	install(requests)
	pass
print("Starting script...")
print("Selamat datang di Aplikasi Snipee.")
print("Open source version, doesnt need authenticate.")

dateTimeObj = datetime.datetime.now()
timestampStr = dateTimeObj.strftime("%H:%M:%S")

def newtime():
	global dateTimeObj
	global timestampStr
	dateTimeObj = datetime.datetime.now()
	timestampStr = dateTimeObj.strftime("%H:%M:%S")

webhook = 0
response = 0
ctypes.windll.kernel32.SetConsoleTitleW("Snipee [Coded by Fallen#0021!]")


# STARTUP EVENT

#print('[',timestampStr,'] This is a test.')
os.system('cls' if os.name == 'nt' else 'clear')
banner = """
███████╗███╗   ██╗██╗██████╗ ███████╗███████╗
██╔════╝████╗  ██║██║██╔══██╗██╔════╝██╔════╝	=-- Programmed --------=
███████╗██╔██╗ ██║██║██████╔╝█████╗  █████╗  	| Written & Coded by   |
╚════██║██║╚██╗██║██║██╔═══╝ ██╔══╝  ██╔══╝  	| Fallen / Pratamz.    |
███████║██║ ╚████║██║██║     ███████╗███████╗	\===________________===/
╚══════╝╚═╝  ╚═══╝╚═╝╚═╝     ╚══════╝╚══════╝
"""
print(banner)
print("Flashsale Sniper [Platform : Shopee Edition] Version 1.2")
print("OPEN SOURCE VERSION, DO NOT RESELL OR ILLEGALLY USE.")
print("Proudly coded with <3 by Fallen (me). Telegram : @FallenV4")
print("");
print("Metode tersebut private, untuk mendapatkan Software Key. Harap hubungi");
print("@FallenV4 di Telegram atau Fallen#0021 via Discord. Thank you!")
producturl = input("Masukkan URL Product: ")
username = input("Masukkan Username Shopee: ")
password = input("Masukkan Password Shopee: ")
os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("Flashsale Sniper [Platform : Shopee Edition] Version 1.2")
print("OPEN SOURCE VERSION, DO NOT RESELL OR ILLEGALLY USE.")
print("Proudly coded with <3 by Fallen (me). Telegram : @FallenV4")
print("");
print("Mohon masukkan metode pembayaran yang ingin dipakai")
print("[1] : ShopeePay (Pastikan Saldo Cukup)")
print("[2] : Bank BCA (Cek Otomatis)")
print("[3] : Bank Mandiri (Cek Otomatis)")
print("[4] : Bank BNI (Cek Otomatis)")
print("[5] : Bank BRI (Cek Otomatis)")
print("[6] : Bank Syariah Mandiri (Cek Otomatis)")
pembayaran = int(input("Pilihan metode pembayaran (1-6) >"))
pakelog = input("Apakah anda ingin memantau aktivitas Sniping via Discord? (y/n) >")
if pakelog == "y":
	print("Masukkan URL Webhook Discord untuk Aktivitas Pemantauan")
	logs = input("Webhook URL >")
	# PREPARATION EVENT
	print("Pemantauan sniping telah diaktifkan.")
	time.sleep(2)
else:
	logs = "fuck off lol"
	print("Pemantauan sniping telah dinonaktifkan.")
	time.sleep(2)

os.system('cls' if os.name == 'nt' else 'clear')
print(banner)
print("Flashsale Sniper [Platform : Shopee Edition]")
print("")
print("The date and time now is",strftime("%Y-%m-%d %H:%M:%S", gmtime()))
print("Please ensure you're using the best quality proxy possible!.")
print("")
print("Awaiting for the time to manual prevent bot detection...");


# MAIN EVENTS

# LOGGING IN TO THE ACCOUNT

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless")
browser = webdriver.Chrome(options=option)
browser.get("https://shopee.co.id/buyer/login")
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button"))
    )
finally:
	newtime()
print("[",timestampStr,"]""[INFO :] SNIPING START!")
dateTimeObj = datetime.datetime.now()
print("[",timestampStr,"]""[INFO :] LOGGING INTO ACCOUNT")
account = browser.find_elements_by_class_name("_56AraZ")
loginbtn = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button")
account[0].send_keys(username)
account[1].send_keys(password)
time.sleep(0.5)
loginbtn.click()
time.sleep(2)

# START SNIPING

newtime()
print("[",timestampStr,"]""[INFO :] LOGIN ACTIVITY DONE, NOW SNIPING...")
webhook = DiscordWebhook(url=logs, content='[INFO :] LOGIN ACTIVITY DONE, NOW SNIPING...')
if pakelog == "y":
	response = webhook.execute()
newtime()
print("[",timestampStr,"]""[INFO :] REDIRECTING INTO THE SPECIFIED PRODUCT URL...")
webhook = DiscordWebhook(url=logs, content='[INFO :] REDIRECTING INTO THE SPECIFIED PRODUCT URL...')
if pakelog == "y":
	response = webhook.execute()

browser.get(producturl)

newtime()
print("[",timestampStr,"]""[INFO :] CHECKING IF PRODUCT VARIANT EXISTS...")
webhook = DiscordWebhook(url=logs, content='[INFO :] CHECKING IF PRODUCT VARIANT EXISTS...')
hasvariant = 1
if pakelog == "y":
	response = webhook.execute()

try:
	element = WebDriverWait(browser, 1).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button"))
    )

except TimeoutException:
	newtime()
	print("[",timestampStr,"]""[INFO :] NO PRODUCT VARIANT FOUND, CONTINUING SNIPING PROCESS...")
	webhook = DiscordWebhook(url=logs, content='[INFO :] NO PRODUCT VARIANT FOUND, CONTINUING SNIPING PROCESS...')
	hasvariant = 0
	if pakelog == "y":
		response = webhook.execute()

if hasvariant == 1:
	productvariant = browser.find_elements_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[4]/div/div[2]/div/div[1]/div/button")
	print(productvariant)
	newtime()
	print("[",timestampStr,"]""[INFO :] VARIANT PRODUK DITEMUKAN, SILAHKAN KETIK NOMOR LIST VARIANT")
	webhook = DiscordWebhook(url=logs, content='[INFO :] VARIANT PRODUK DITEMUKAN, SILAHKAN KETIK NOMOR LIST VARIANT DI CONSOLE')
	if pakelog == "y":
		response = webhook.execute()
	inputvariant = int(input("Masukkan nomor variant product >"))

while True:
	try:
	    element = WebDriverWait(browser, 1).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]")))
	    belisekarang = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]")
	    newtime()
	    print("[",timestampStr,"]""[INFO :] ORDER BUTTON FOUND, ATTEMPTING TO SUBMIT...")
	    webhook = DiscordWebhook(url=logs, content='[INFO :] ORDER BUTTON FOUND, ATTEMPTING TO SUBMIT...')
	    if pakelog == "y":
	    	response = webhook.execute()
	    break
	except NoSuchElementException:
		newtime()
		print("[",timestampStr,"]""[INFO :] ORDER BUTTON NOT FOUND, REFRESHING THE PAGE...")
		webhook = DiscordWebhook(url=logs, content='[INFO :] ORDER BUTTON NOT FOUND, REFRESHING THE PAGE...')
		if pakelog == "y":
			response = webhook.execute()
		browser.refresh()
		continue
	except TimeoutException:
		newtime()
		print("[",timestampStr,"]""[INFO :] ORDER BUTTON NOT FOUND, REFRESHING THE PAGE...")
		webhook = DiscordWebhook(url=logs, content='[INFO :] ORDER BUTTON NOT FOUND, REFRESHING THE PAGE...')
		if pakelog == "y":
			response = webhook.execute()
		browser.refresh()
		continue
print(belisekarang.is_enabled())
btnclass = belisekarang.get_attribute("class")
print(btnclass)

while True:
	if 'disabled' in btnclass:
		newtime()
		webhook = DiscordWebhook(url=logs, content='[INFO :] ORDER BUTTON DISABLED, REFRESHING THE PAGE...')
		if pakelog == "y":
			response = webhook.execute()
		print("[",timestampStr,"]""[INFO :] ORDER BUTTON DISABLED!, REFRESHING THE PAGE...")
		browser.refresh()
		element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]")))
		belisekarang = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[2]/div[2]/div[3]/div/div[5]/div/div/button[2]")
		btnclass = belisekarang.get_attribute("class")
	else:
		if hasvariant == 1:
			productvariant[inputvariant].click()
		belisekarang.click()
		newtime()
		webhook = DiscordWebhook(url=logs, content='[INFO :] ORDER BUTTON ENABLED, ATTEMPTING TO PUT ITEM IN CART...')
		if pakelog == "y":
			response = webhook.execute()
		print("[",timestampStr,"]""[INFO :] ORDER BUTTON ENABLED!, ATTEMPTING TO PUT ITEM IN CART...")
		break

newtime()
print("[",timestampStr,"]""[INFO :] SUCCESSFULLY PUT ITEM INTO CART!")
webhook = DiscordWebhook(url=logs, content='[INFO :] SUCCESSFULLY PUT ITEM INTO CART!')
if pakelog == "y":
	response = webhook.execute()

try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button"))
    )
finally:
	checkout = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div[3]/div[2]/div[7]/div[5]/button")

# START CHECKOUT PR
newtime()
print("[",timestampStr,"]""[INFO :] ATTEMPTING TO CHECKOUT ITEM.")
browser.execute_script("arguments[0].click();", checkout)
#checkout.click()
webhook = DiscordWebhook(url=logs, content='[INFO :] ATTEMPTING TO CHECKOUT ITEM.')
if pakelog == "y":
	response = webhook.execute()

try:
	element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[1]/button"))
    )
finally:
	shopeepay =  browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[1]/button")

try:
	element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[3]/button"))
    )
finally:
	bankmethod =  browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[1]/div[2]/span[3]/button")

if pembayaran == 1:
	shopeepay.click()

elif pembayaran == 2:
	bankmethod.click()
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK AS PAYMENT METHOD.")
	try:
		element = WebDriverWait(browser, 10).until(
	    	EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div"))
	    )
	finally:
		bankbca = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[1]/div")
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK BCA AS THE BANK.")
	webhook = DiscordWebhook(url=logs, content='[INFO :] SELECTING BANK BCA AS THE BANK.')
	if pakelog == "y":
		response = webhook.execute()
	bankbca.click()

elif pembayaran == 3:
	bankmethod.click()
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK AS PAYMENT METHOD.")
	try:
		element = WebDriverWait(browser, 10).until(
	    	EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div"))
	    )
	finally:
		mandiri1 = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[2]/div")
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK MANDIRI AS THE BANK.")
	webhook = DiscordWebhook(url=logs, content='[INFO :] SELECTING BANK MANDIRI AS THE BANK.')
	if pakelog == "y":
		response = webhook.execute()
	mandiri1.click()

elif pembayaran == 4:
	bankmethod.click()
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK AS PAYMENT METHOD.")
	try:
		element = WebDriverWait(browser, 10).until(
	    	EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div"))
	    )
	finally:
		bankbni = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div")
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK BNI AS THE BANK.")
	webhook = DiscordWebhook(url=logs, content='[INFO :] SELECTING BANK BNI AS THE BANK.')
	if pakelog == "y":
		response = webhook.execute()
	bankbni.click()

elif pembayaran == 5:
	bankmethod.click()
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK AS PAYMENT METHOD.")
	try:
		element = WebDriverWait(browser, 10).until(
	    	EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div"))
	    )
	finally:
		bankbri = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[4]/div")
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK BRI AS THE BANK.")
	webhook = DiscordWebhook(url=logs, content='[INFO :] SELECTING BANK BRI AS THE BANK.')
	if pakelog == "y":
		response = webhook.execute()
	bankbri.click()

elif pembayaran == 6:
	bankmethod.click()
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING BANK AS PAYMENT METHOD.")
	try:
		element = WebDriverWait(browser, 10).until(
	    	EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[5]"))
	    )
	finally:
		mandirisyariah = browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[3]/div[4]/div[1]/div/div[2]/div[1]/div[2]/div[5]")
	newtime()
	print("[",timestampStr,"]""[INFO :] SELECTING MANDIRI SYARI'AH AS THE BANK.")
	webhook = DiscordWebhook(url=logs, content='[INFO :] SELECTING MANDIRI SYARIAH AS THE BANK.')
	if pakelog == "y":
		response = webhook.execute()
	mandirisyariah.click()

else:
	print("Invalid payment method specified!, please try again later.")
	print("Sniping failed!")

# BUAT ORDER
try:
    element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "stardust-button"))
    )
finally:
	newtime()
	print("[",timestampStr,"]""[INFO :] CREATING YOUR ORDER.")
webhook = DiscordWebhook(url=logs, content='[INFO :] CREATING YOUR ORDER.')
if pakelog == "y":
	response = webhook.execute()
makeorder = browser.find_element_by_class_name("stardust-button")
browser.execute_script("arguments[0].click();", makeorder)
#makeorder.click()

# END EVENT
newtime()
print("[",timestampStr,"]""[INFO :] SUCCESSFULLY ATTEMPTED TO SNIPE PRODUCT!")
webhook = DiscordWebhook(url=logs, content='[INFO :] SUCCESSFULLY ATTEMPTED TO SNIPE PRODUCT!')
if pakelog == "y":
	response = webhook.execute()
newtime()
print("[",timestampStr,"]""[INFO :] PLEASE CHECK YOUR ORDER LIST ON UNPAID!.")
webhook = DiscordWebhook(url=logs, content='[INFO :] PLEASE CHECK YOUR ORDER LIST ON UNPAID!')
if pakelog == "y":
	response = webhook.execute()
print("Your request product has been sniped at",strftime("%Y-%m-%d %H:%M:%S", gmtime()))
time.sleep(2)
webhook = DiscordWebhook(url=logs, content='Your request product has been successfully sniped!')
if pakelog == "y":
	response = webhook.execute()
print("We will close our script by 10 seconds.")
webhook = DiscordWebhook(url=logs, content='The console will close at few seconds.')
if pakelog == "y":
	response = webhook.execute()
time.sleep(10)

# Semoga bermanfaat!.
