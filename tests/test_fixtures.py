import pytest
from selene import browser, by
from conftest import mobile_browser, desktop_browser


def test_mobile_browser(mobile_browser):
    browser.open("https://github.com/")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()


def test_desktop_browser(desktop_browser):
    browser.open("https://github.com/")
    browser.element(by.text("Sign up")).click()