from pages.base_page import BasePage
from pages.locators import Signup
from playwright.sync_api import sync_playwright
import time


class SignupPage(BasePage):


    def __init__(self, page):
        super().__init__(page)
        self.name_input = page.locator(Signup.INPUT_NAME)
        self.email_input = page.locator(Signup.INPUT_MAIL)
        self.signup_button = page.locator(Signup.BUTTON_SIGNUP)

    def start_signup(self, name, email):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()
        time.sleep(5)

    # def get_brauser(self, name, email):
    #     url =  "https://automationexercise.com/login"
    #     with sync_playwright as  playwright:
    #         browser = playwright.chromium.launch(heandless = False)
    #         context = browser.new_context()
    #         page = context.new_context()
    #         page.goto(url)

    #         self.start_signup(name, email)

    #         context.close()
    #         browser.close()