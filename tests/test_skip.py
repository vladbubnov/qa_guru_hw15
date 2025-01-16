import pytest
from selene import browser, by
from conftest import setup_browser


def test_desktop_skip(setup_browser):
    if setup_browser == "mobile":
        pytest.skip("Это мобильное разрешение")
    browser.open("https://github.com/")
    browser.element(by.text("Sign up")).click()


def test_mobile_skip(setup_browser):
    if setup_browser == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com/")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()
