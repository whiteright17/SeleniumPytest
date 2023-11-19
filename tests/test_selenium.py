from selenium.webdriver.common.by import By


def test_google_search(browser):
    browser.get("https://www.google.com.ua")
    search_box = browser.find_element(By.NAME, "q")
    search_query = "Hello World!"
    search_box.send_keys(search_query)
    search_box.submit()
    browser.implicitly_wait(5)
    actual_result = browser.title
    expected_result = f"{search_query} - Поиск в Google"
    assert expected_result in actual_result
