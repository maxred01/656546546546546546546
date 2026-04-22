import re
from playwright.sync_api import Playwright, sync_playwright, expect, APIRequestContext, Page
from conftest import api_request_context
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_last_created_issue_should_be_on_the_server(api_request_context: APIRequestContext) -> None:
    new_issue = api_request_context.get(url='/booking')
    print(new_issue.ok)
    print(new_issue.json())


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://hoster.by/")
    page.get_by_role("button", name="Принять").click()
    page.get_by_text("Домены и хостинг").click()
    page.get_by_text("Облачные сервисы", exact=True).click()
    page.get_by_role("banner").get_by_text("Кибербезопасность").click()
    page.locator("div").filter(has_text="Кибербезопасность").nth(5).click()
    page.get_by_role("textbox", name="Введите домен или слово").click()
    page.get_by_role("textbox", name="Введите домен или слово").fill("demodemo")
    page.get_by_role("textbox", name="Введите домен или слово").press("Enter")
    page.locator("#domain_by").click()
    page.locator("#domain_of_by").click()
    page.locator("[id=\"domain_бел\"]").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
