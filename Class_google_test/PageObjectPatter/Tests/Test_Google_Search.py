from selenium import webdriver
import time
import pytest
from Pages.Google_Result import result_page
from Pages.Google_Search import google_page


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver

    driver.quit()

def test_wyszukiwanie(driver):

    search_page= google_page(driver)
    search_page.open()

    assert "Google" in driver.title #sprawdzanie czy zaladowala sie poprawna strona

    search_page.accept_cookies()

    search_page.search("pogoda myslowice")

    driver.set_window_size(1000, 1000)

    time.sleep(20)  # zatrzymanie skryptu na 10 sekund

    result_page(driver)

    results= result_page.get_results()  #znalezienie wynikow wyszukiwania

    assert len(results) > 0, "brak wynikow" #sprawdzenie czy znaleziono jakies wyniki
    driver.quit()