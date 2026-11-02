import pytest
import uuid
from playwright.sync_api import expect



class TestSignup:

    def test_signup_with_new_email_opens_account_info_form(self, signup_page):

        email = f"ivan_{uuid.uuid4().hex[:8]}@test.com"
        

        signup_page.start_signup("Ivan", email)

        expect(signup_page.page).to_have_url("https://automationexercise.com/signup")
        expect(signup_page.page.get_by_text("Enter Account Information")).to_be_visible()