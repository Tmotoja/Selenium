from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# inicjalizacja przeglądarki Chrome
driver = webdriver.Chrome()

# implicitly wait - oczekiwanie na pojawie się każdego elementu na stronie przez maksymanie X (podajemy jako parametr) sekund
# driver.implicitly_wait(5)

url = "https://www.w3schools.com/"

# upobranie konkretnego adresu w przeglarce
driver.get(url)

# rozmiar okna
driver.maximize_window()

# ciasteczka
time.sleep(5)
accept_cookies2 = driver.find_element("id", "accept-choices")
accept_cookies2.click()
# driver.find_element("id", "accept-choices").click()

# Tutorials
menu = driver.find_element("id", "navbtn_tutorials")
menu.click()
#webdriver.ActionChains(driver).move_to_element(menu).click().perform()

# learn HTML
learnHTML = driver.find_element('xpath', '//*[@id="tutorials_html_css_links_list"]/div[1]/a[1]')
#learnHTML = driver.find_element('xpath', '//a[@title="HTML Tutorial"]')
learnHTML.click()

# explicitly wait - czekamy na konketny element
wait = WebDriverWait(driver,10,0.5)
# warunek oczekiwania
wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[71]')))
# gdyby był problem, to można uzyc starej metody
# wait.until(EC.visibility_of_element_located((By.XPATH , '//*[@id="leftmenuinnerinner"]/a[43]')))
# wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))

# menu 'tag list'
menuTagList = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[71]')
menuTagList.click()

# menu 'input'
menuInput2 = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/div/a[59]')
menuInput2.click()

# link 'disable'
linkDisable = driver.find_element('xpath', '//*[@id="main"]/table[2]/tbody/tr[8]/td[1]/a')
linkDisable.click()

# kliknij 'Try it yourself'
tryItYourself = driver.find_element('xpath', '//*[@id="main"]/div[2]/a')
tryItYourself.click()

print("Aktualne okno: ", driver.title)

# przełaczenie sie na nową zakładke
# obecna zakladka
currentWindow = driver.current_window_handle

# lista wszystkich zakladek (okienek)
windowsNames = driver.window_handles

# sprwdzic w petli, czy dana zakladka nie jest aktualna
for window in windowsNames:
    if window != currentWindow:
        driver.switch_to.window(window)

print("Aktualne okno po pętli: ", driver.title)

# przełaczenie do iframe
driver.switch_to.frame(driver.find_element('id', 'iframeResult'))

# wprowadz imie
name = driver.find_element('xpath', '//*[@id="fname"]')
name.send_keys("Natalia")


#zatrzymanie skryptu
time.sleep(500)

# zamkniecie przegladarki
driver.quit()