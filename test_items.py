def test_find_button(browser):
    #correct link:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    # not correct lenk:
    # link = "http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    assert browser.find_elements_by_css_selector("button.btn-add-to-basket"), "Button not find!"

