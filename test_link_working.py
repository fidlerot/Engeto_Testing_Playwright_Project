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

def test_link_o_rozbitem_prasatku(page):
    page.goto("https://rozbiteprasatko.cz/")
  
# Wait for and click the cookies button
    page.wait_for_selector('text="Odmítnout"',timeout=60000)  #cekam na tlacitko nez se nacte
    button = page.query_selector('text="Odmítnout"')
    assert button is not None, 'Button not found' 
    button.click()

# Verify the existence of the "O Rozbitém prasátku" link and click it
    link_selector = 'a.elementor-item[href="https://rozbiteprasatko.cz/o-rozbitem-prasatku/"]'
    page.wait_for_selector(link_selector, timeout=60000)
    link = page.query_selector(link_selector)
    assert link is not None, '"O Rozbitém prasátku" link not found'
    link.click()

 # Verify the URL after clicking the link
    assert "https://rozbiteprasatko.cz/o-rozbitem-prasatku/" in page.url, "Not redirected to 'O Rozbitém prasátku' page"
    print ("Test completed succesfully")