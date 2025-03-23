from selenium import webdriver
import time

#inicjalizacja przegladarki chrome
driver= webdriver.Chrome()

url= "https://www.google.pl/"
new_url= "https://www.wp.pl/"

driver.get(url)

#driver.maximize_window()
driver.set_window_size(1000, 1000)    

driver.execute_script("window.open('');") #otwarcie nowej karty

driver.switch_to.window(driver.window_handles[1]) #zmiana karty

driver.get(new_url) #otwarcie nowej strony

time.sleep(10) #zatrzymanie skryptu na 10 sekund

driver.quit() #zamkniecie przegladarki

#driver.close()nie zamyka przegladarki, tylko karte
#driver.quit()zamyka przegladarke

