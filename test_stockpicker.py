from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("file:///C:/Users/mirac/OneDrive/Desktop/SED500_Lab_4/files/StockPicker.html")

def test_enter_symbol():
    symbol_input = driver.find_element(By.ID, "symbol")
    symbol_input.clear()
    symbol_input.send_keys("AAPL")
    assert symbol_input.get_attribute("value") == "AAPL", "Symbol input is not working properly."

def test_select_category():
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("balance-sheet-statement")
    assert category_select.first_selected_option.get_attribute("value") == "balance-sheet-statement", \
        "Category selection is not working properly."

# RE-01.6
def test_submit_query():
    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()
    time.sleep(2)
    assert "data" in driver.page_source, "Submit query did not display any data."

# RE-01.7 & RE-08
def test_reset_button_and_default_ui():
    reset_button = driver.find_element(By.ID, "reset")
    reset_button.click()

    symbol_input = driver.find_element(By.ID, "symbol")
    assert symbol_input.get_attribute("value") == "", "Reset button did not clear the symbol input."

    category_select = Select(driver.find_element(By.ID, "category"))
    assert category_select.first_selected_option.get_attribute("value") == "income-statement", \
        "Reset button did not reset the category to default."

    screener_fields = driver.find_elements(By.CLASS_NAME, "screener")
    for field in screener_fields:
        assert "hidden" in field.get_attribute("class"), "Reset button did not hide screener fields."

# RE-02.2
def test_stock_screener_category():
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("stock-screener")
    stock_screener = Select(driver.find_element(By.ID, "stock-screener"))
    stock_screener.select_by_value("marketCapMoreThan")
    assert stock_screener.first_selected_option.get_attribute("value") == "marketCapMoreThan", \
        "Stock screener category selection is not working properly."

# RE-02.3
def test_stock_screener_value():
    category_select = Select(driver.find_element(By.ID, "category"))
    category_select.select_by_value("stock-screener")
    value_input = driver.find_element(By.ID, "stock-screener-value")
    value_input.clear()
    value_input.send_keys("1000000000")
    assert value_input.get_attribute("value") == "1000000000", "Stock screener value input is not working properly."

# RE-03
def test_display_data():
    test_submit_query() 
    data_section = driver.find_element(By.ID, "data")
    assert data_section.is_displayed(), "Data section is not displayed after a query."

try:
    test_enter_symbol()
    print("Test RE-01.3 passed.")
    test_select_category()
    print("Test RE-01.5 passed.")
    test_submit_query()
    print("Test RE-01.6 passed.")
    test_reset_button_and_default_ui()
    print("Test RE-01.7 & RE-08 passed.")
    test_stock_screener_category()
    print("Test RE-02.2 passed.")
    test_stock_screener_value()
    print("Test RE-02.3 passed.")
    test_display_data()
    print("Test RE-03 passed.")
finally:
    driver.quit()
