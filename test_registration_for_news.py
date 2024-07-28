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

@pytest.mark.parametrize("email", [
'foo@bar.baz',
'baz@bar.com',
'hello@gmail.com',
'who@hotmail.com',
])

def test_registration_for_news(page,email):
    page.goto("https://rozbiteprasatko.cz/")
    page.wait_for_selector("input[name='form_fields[email]']",timeout=60000)
    page.locator("input[name='form_fields[email]']").fill(email)
    submit_button = page.get_by_role("button", name="Potvrdit e-mail")
    submit_button.click()
    
    page.wait_for_selector('h1.elementor-heading-title.elementor-size-default', timeout=60000)
    confirmation = page.locator("text='Poděkování'")
    assert confirmation.text_content() == "Poděkování"
    
    print ("Test completed succesfully")

