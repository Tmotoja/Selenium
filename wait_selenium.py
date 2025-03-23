from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

#inicjalizacja przegladarki chrome
driver= webdriver.Chrome()
driver.set_window_size(1000, 1000) 

#driver.implicitly_wait(5) #czekanie na elementy na stronie przez max 5 sec

url= "https://www.w3schools.com/"

driver.get(url)
#time.sleep(3)

time.sleep(3)
cookies_web= driver.find_element("id", "accept-choices")
cookies_web.click()

tutorial_tab= driver.find_element("id", "navbtn_tutorials")
#tutorial_tab.click() lub dugi sposob \/
webdriver.ActionChains(driver).move_to_element(tutorial_tab).click().perform()

tutorial_html= driver.find_element('xpath', '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
tutorial_html.click()

driver.save_screenshot("tutorial_html.png"+ str(time.time()))

htmlinput= driver.find_element('xpath', '//*[@id="main"]/div[4]/a')

wait= WebDriverWait(driver, 60, 1) #10 sekund na znalezienie elementu, sprawdzanie co 0.5 sekundy 
#wait.until(EC.visibility_of_element_located('xpath', '//*[@id="main"]/div[4]/a'))
#wait.until(lambda x: len(x.find.element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]'))) #czeka na pojawienie sie elementu

webdriver.ActionChains(driver).move_to_element(htmlinput).click().perform()
htmlinput.click()

print("aktualne okno: ",driver.title)

current_window= driver.current_window_handle
windows= driver.window_handles

for w in windows:
    if w != current_window:
        driver.switch_to.window(w)
driver.save_screenshot("htmlinput.png"+ str(time.time())) #zapisanie screena strony
time.sleep(20)

#driver.quit() #zamkniecie przegladarki