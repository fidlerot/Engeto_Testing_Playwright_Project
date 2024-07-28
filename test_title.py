# Test1 - otevru stranku www.rozbiteprasatko.cz, odkliknu cookies Odmítnout a zkontroluji, ze souhlasi titulek stranky
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_title_name(page):
    page.goto("https://rozbiteprasatko.cz/")
    page.wait_for_selector('text="Odmítnout"',timeout=60000) 
    button = page.query_selector('text="Odmítnout"')
    assert button is not None, 'Button not found' 
    button.click()
    title = page.title()
    assert title=="Rozbité prasátko. Váš odrazový můstek do světa peněz!"
    print("Test completed succesfully")

  