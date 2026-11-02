import pytest
from pages.signup_page import SignupPage



@pytest.fixture
def signup_page(page):
    signup = SignupPage(page)
    signup.open()
    return signup