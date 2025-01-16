import pytest
from selene import browser, by
from conftest import mobile_browser, desktop_browser


@pytest.mark.parametrize("mobile_browser", [(360, 740), (375, 667), (412, 915)], indirect=True)
def test_mobile_browser(mobile_browser):
    browser.open("https://github.com/")
    browser.element("[class='Button-content']").click()
    browser.element(by.text("Sign up")).click()


@pytest.mark.parametrize("desktop_browser", [(1600, 900), (1344, 1008), (1280, 720)], indirect=True)
def test_desktop_browser(desktop_browser):
    browser.open("https://github.com/")
    browser.element(by.text("Sign up")).click()