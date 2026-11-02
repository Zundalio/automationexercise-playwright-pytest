class BasePage:
    #TODO в конфиг перенести
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(self.URL)