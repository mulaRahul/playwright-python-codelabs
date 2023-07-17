from playwright.sync_api import Page


def solution(page: Page) -> Page:
    # visit test site
    page.goto("https://bootswatch.com/default/")
    
    # store your locator 👇
    locator = ...

    # return locator for evaluation
    return locator
