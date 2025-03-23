from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

def test_wyszukiwanie(driver):

    url = "https://www.google.pl/"

    driver.get(url)

    assert "Google" in driver.title #sprawdzanie czy zaladowala sie poprawna strona

    accept_cookies = driver.find_element("id", "L2AGLb")  # znalezienie przycisku akceptacji cookies

    accept_cookies.click()

    searchbar = driver.find_element("name", "q")  # znalezienie paska wyszukiwania

    searchbar.click()
    searchbar.send_keys("pogoda myslowice")  # wpisanie tekstu do paska wyszukiwania
    # searchbar.submit() METODA 1 #wyslanie formularza
    searchbar.send_keys(Keys.ENTER)  # METODA 2 #wyslanie formularza

    driver.set_window_size(1000, 1000)

    time.sleep(20)  # zatrzymanie skryptu na 10 sekund

    results= driver.find_elements("css selector", "h3")  #znalezienie wynikow wyszukiwania
    print("dlugosc listy", len(results))

    assert len(results) > 0, "brak wynikow"
    driver.quit()  # zamkniecie przegladarki
