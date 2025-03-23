from selenium import webdriver
import time

driver =webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://www.kurs-selenium.pl/demo/")

# # uzupełnic dane w formularzu
city = driver.find_element('xpath', '//span[text()="Search by Hotel or City Name"]')
# time.sleep(200)
city.click()
city = driver.find_element('xpath', '//*[@id="select2-drop"]/div/input')
city.send_keys("Dubai")
# kliknieci w dopasowane miasto
city = driver.find_element('xpath', '//*[@id="select2-drop"]/ul/li/ul/li/div')
city.click()

#checkin i checkout
checkin = driver.find_element('name', 'checkin')
checkin.send_keys('23/03/2025')
checkout = driver.find_element('name', 'checkout')
checkout.send_keys('24/03/2025')

# uzupelnienie liczby przyjezdnych
travelleres = driver.find_element('id', 'travellersInput')
travelleres.click()

# dorosli i dzieci
adult = driver.find_element('id', 'adultInput')
adult.clear()
adult.send_keys(1)

child = driver.find_element('id', 'childInput')
child.clear()
child.send_keys(2)

# wyszukac wyniki
search = driver.find_element('xpath', '//*[@id="hotels"]/form/div[5]/button')
search.click()

# nastepna strona

# sprawdzic wyniki
hotels= driver.find_elements('xpath', '//h4[contains(@class, "list_title")]')
print(len(hotels))

hotels_names = [hotel.get_attribute("textContent") for hotel in hotels]
print(hotels_names)

assert hotels_names[0] == "Jumeirah Beach Hotel"
assert hotels_names[1] == "Oasis Beach Tower"
assert hotels_names[2] == "Rose Rayhaan Rotana"
assert hotels_names[3] == "Hyatt Regency Perth"
time.sleep(15)
driver.quit()