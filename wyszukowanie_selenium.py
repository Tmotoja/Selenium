from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#inicjalizacja przegladarki chrome
driver= webdriver.Chrome()

url= "https://www.google.pl/"

driver.get(url)

accept_cookies= driver.find_element("id", "L2AGLb") #znalezienie przycisku akceptacji cookies

accept_cookies.click()

searchbar= driver.find_element("name", "q") #znalezienie paska wyszukiwania

searchbar.click()
searchbar.send_keys("pogoda myslowice") #wpisanie tekstu do paska wyszukiwania
  #searchbar.submit() METODA 1 #wyslanie formularza
searchbar.send_keys(Keys.ENTER) #METODA 2 #wyslanie formularza

driver.set_window_size(1000, 1000)    

time.sleep(6000) #zatrzymanie skryptu na 10 sekund

driver.quit() #zamkniecie przegladarki
