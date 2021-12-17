import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_for_add_items_in_basket(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element_by_css_selector("button[type='submit']")
