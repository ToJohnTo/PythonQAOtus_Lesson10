from explicit_wait import MyWaits


url = "http://localhost/index.php?route=product/product&path=57&product_id=49"


def test_element_by_id(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.element("#logo")
    # browser.find_element(By.ID, "logo")
    my_waits.element("#search")
    # browser.find_element_by_id("search")


# def test_element_by_link_text(browser):
#     browser.get(url)
#     browser.find_element_by_partial_link_text("Galaxy Tab")


def test_elements_by_css_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".thumbnail")
    # browser.find_elements(By.CSS_SELECTOR, ".thumbnail")


def test_element_by_class_name_selector(browser):
    my_waits = MyWaits(browser)
    browser.get(url)
    my_waits.elements(".input-group-btn")
    # browser.find_elements_by_class_name("input-group-btn")
